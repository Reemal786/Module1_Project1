"""
embed_retrieve.py

Purpose:
1. Load chunks from ingest.py
2. Embed chunks using all-MiniLM-L6-v2
3. Store chunks in ChromaDB with metadata
4. Retrieve the top-k most relevant chunks for a query
"""

import chromadb
from sentence_transformers import SentenceTransformer

from ingest import build_chunks


# -----------------------------
# Settings from planning.md
# -----------------------------

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "medical_assistant_study_guide"
TOP_K = 5


# -----------------------------
# 1. Load embedding model
# -----------------------------

print("Loading embedding model...")

embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

print("Embedding model loaded.")


# -----------------------------
# 2. Set up ChromaDB
# -----------------------------

# PersistentClient saves the database to disk.
# This means your vector database will still exist after the script closes.
client = chromadb.PersistentClient(path="chroma_db")

# Get the collection if it already exists, or create it if it does not.
collection = client.get_or_create_collection(name=COLLECTION_NAME)


# -----------------------------
# 3. Build vector store
# -----------------------------

def build_vector_store():
    """
    Loads chunks from the ingestion pipeline, embeds them,
    and stores them in ChromaDB.

    Each chunk gets:
    - id: unique chunk ID
    - document: the actual text chunk
    - embedding: vector representation of the chunk
    - metadata: source document and chunk position
    """

    chunks = build_chunks()

    print(f"Loaded {len(chunks)} chunks from ingestion pipeline.")

    # Clear old collection data so rerunning the script does not duplicate chunks.
    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])
        print("Cleared old chunks from ChromaDB.")

    texts = []
    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        texts.append(chunk["text"])
        ids.append(chunk["chunk_id"])

        metadatas.append({
            "source": chunk["source"],
            "chunk_index": i
        })

    print("Creating embeddings...")

    embeddings = embedding_model.encode(texts).tolist()

    print("Embeddings created.")

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(texts)} chunks in ChromaDB.")


# -----------------------------
# 4. Retrieval function
# -----------------------------

def retrieve(query, top_k=TOP_K):
    """
    Accepts a user query and returns the top-k most relevant chunks.

    Steps:
    1. Embed the query using the same model used for documents.
    2. Search ChromaDB for similar chunk embeddings.
    3. Return chunk text, source metadata, and distance scores.

    Lower distance usually means a closer/better match.
    """

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved_chunks = []

    for i in range(len(results["ids"][0])):
        retrieved_chunks.append({
            "id": results["ids"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "chunk_index": results["metadatas"][0][i]["chunk_index"],
            "text": results["documents"][0][i],
            "distance": results["distances"][0][i]
        })

    return retrieved_chunks


# -----------------------------
# 5. Test retrieval
# -----------------------------

if __name__ == "__main__":
    build_vector_store()

    test_queries = [
        "What does HIPAA stand for?",
        "What is a normal adult heart rate?",
        "What are the steps for taking blood pressure?",
    ]

    for query in test_queries:
        print("\n" + "=" * 100)
        print(f"QUERY: {query}")
        print("=" * 100)

        results = retrieve(query, top_k=5)

        for result in results:
            print("\n--- Retrieved Chunk ---")
            print(f"Source: {result['source']}")
            print(f"Chunk Index: {result['chunk_index']}")
            print(f"Distance: {result['distance']}")
            print(result["text"][:700])