from pathlib import Path
import re
import html
from pypdf import PdfReader

# -----------------------------
# Settings from planning.md
# -----------------------------

DATA_DIR = Path("data")
RAW_DIR = Path("raw_text")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


# -----------------------------
# 1. Load documents
# -----------------------------

def load_pdf(file_path):
    """
    Reads text from a PDF file.
    Each page is extracted and combined into one string.
    """

    reader = PdfReader(file_path)
    text_pages = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text_pages.append(page_text)

    return "\n".join(text_pages)


def load_txt(file_path):
    """
    Reads text from a .txt or .md file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def load_documents():
    """
    Loads all supported files from the data folder.
    Supports:
    - .pdf
    - .txt
    - .md
    """

    documents = []

    for file_path in DATA_DIR.iterdir():
        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            raw_text = load_pdf(file_path)

        elif suffix in [".txt", ".md"]:
            raw_text = load_txt(file_path)

        else:
            continue

        documents.append({
            "source": file_path.name,
            "raw_text": raw_text
        })

    return documents


# -----------------------------
# 2. Save raw text
# -----------------------------

def save_raw_text(documents):
    """
    Saves raw extracted text before cleaning.
    This lets us inspect the original extraction later.
    """

    RAW_DIR.mkdir(exist_ok=True)

    for doc in documents:
        source_name = Path(doc["source"]).stem
        output_path = RAW_DIR / f"{source_name}.txt"

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(doc["raw_text"])


# -----------------------------
# 3. Clean documents
# -----------------------------

def clean_text(text):
    """
    Cleans the document text before chunking.

    Removes:
    - HTML tags
    - HTML entities like &amp; and &nbsp;
    - extra whitespace
    - repeated website boilerplate patterns
    """

    # Convert HTML entities:
    # Example: &amp; becomes &, &nbsp; becomes a space
    text = html.unescape(text)

    # Remove HTML tags if any were copied from webpages
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove common webpage/navigation phrases
    boilerplate_patterns = [
        r"Skip to main content",
        r"Subscribe",
        r"Share this article",
        r"Read more",
        r"Advertisement",
        r"Cookie Policy",
        r"Privacy Policy",
        r"Terms of Use",
        r"Back to top",
        r"Menu",
        r"Search",
        r"Get Free Checklist",
        r"Submit Press Releases",
        r"Editorial Policy",
        r"Mission Statement",
        r"Careers",
        r"Advertise",
        r"Contact Us",
        r"Terms & Conditions",
        r"Trademark Policy",
        r"Accessibility Statement",
        r"Site Map",
        r"All Rights Reserved",
        r"© Copyright.*",
    ]

    for pattern in boilerplate_patterns:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)

    # Replace non-breaking spaces
    text = text.replace("\xa0", " ")

    # Remove repeated spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove too many blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Clean spaces around line breaks
    text = re.sub(r" *\n *", "\n", text)

    # Remove URLs
    text = re.sub(r"https?://\S+", " ", text)

    # Remove page number patterns like "18 of 18 6/11/2026, 9:49 PM"
    text = re.sub(r"\d+\s+of\s+\d+\s+\d{1,2}/\d{1,2}/\d{4},?\s+\d{1,2}:\d{2}\s*(AM|PM)?", " ", text, flags=re.IGNORECASE)

    # Remove repeated PDF title/footer lines
    text = re.sub(r"HIPAA Training Requirements - Updated for 2026", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"Vital Signs \(Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure\).*", " ", text, flags=re.IGNORECASE)
    
    return text.strip()


# -----------------------------
# 4. Chunk text
# -----------------------------

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """
    Splits text into overlapping chunks, but tries to end chunks at natural
    break points like paragraph breaks, sentence endings, or spaces.

    This avoids chunks ending in the middle of words when possible.
    """

    chunks = []
    start = 0

    while start < len(text):
        target_end = start + chunk_size

        # If this is the last chunk, just take the rest
        if target_end >= len(text):
            chunk = text[start:].strip()
            if chunk:
                chunks.append(chunk)
            break

        # Look for a better ending point near the target end
        window = text[start:target_end]

        # Prefer paragraph break, then sentence ending, then space
        paragraph_break = window.rfind("\n\n")
        sentence_break = max(window.rfind("."), window.rfind("?"), window.rfind("!"))
        space_break = window.rfind(" ")

        if paragraph_break > chunk_size * 0.5:
            end = start + paragraph_break
        elif sentence_break > chunk_size * 0.5:
            end = start + sentence_break + 1
        elif space_break > chunk_size * 0.5:
            end = start + space_break
        else:
            end = target_end

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # Move start forward with overlap
        start = max(end - overlap, start + 1)

    return chunks


# -----------------------------
# 5. Build final chunks
# -----------------------------

def build_chunks():
    """
    Full ingestion pipeline:
    1. Load documents
    2. Save raw text
    3. Clean text
    4. Chunk text
    5. Store source metadata with each chunk
    """

    documents = load_documents()
    save_raw_text(documents)

    all_chunks = []

    for doc in documents:
        source = doc["source"]
        cleaned_text = clean_text(doc["raw_text"])
        chunks = chunk_text(cleaned_text)

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source": source,
                "chunk_id": f"{Path(source).stem}_chunk_{i}",
                "text": chunk
            })

    return all_chunks


# -----------------------------
# 6. Test the script
# -----------------------------

if __name__ == "__main__":
    chunks = build_chunks()

    print(f"\nTotal chunks created: {len(chunks)}")

    print("\nPrinting 5 representative chunks:\n")

    for chunk in chunks[:5]:
        print("=" * 80)
        print(f"Source: {chunk['source']}")
        print(f"Chunk ID: {chunk['chunk_id']}")
        print("-" * 80)
        print(chunk["text"])
        print()

    if len(chunks) < 50:
        print("Warning: You have fewer than 50 chunks. Your chunks may be too large.")

    if len(chunks) > 2000:
        print("Warning: You have more than 2,000 chunks. Your chunks may be too small.")