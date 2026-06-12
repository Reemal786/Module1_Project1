"""
query.py

Purpose:
1. Retrieve relevant chunks from ChromaDB.
2. Send those chunks to Llama through Groq.
3. Return a grounded answer with source attribution.

Important:
The model is instructed to answer ONLY from retrieved context.
Sources are added programmatically so the LLM cannot forget them.
"""

import os
from dotenv import load_dotenv
from groq import Groq

from embed_retrieve import retrieve


# -----------------------------
# Load API key from .env
# -----------------------------

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Make sure it is in your .env file.")


# -----------------------------
# Initialize Groq client
# -----------------------------

client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "llama-3.3-70b-versatile"


# -----------------------------
# Prompt builder
# -----------------------------

def build_prompt(question, retrieved_chunks):
    """
    Builds the prompt that will be sent to Llama.

    The retrieved chunks become the ONLY allowed source of information.
    """

    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"[Source {i}: {chunk['source']} | Chunk {chunk['chunk_index']}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a Medical Assistant Study Guide chatbot.

Answer the user's question using ONLY the information in the provided context.

Rules:
- Do not use outside knowledge.
- Do not guess.
- If the context does not contain enough information, say:
  "I don't have enough information on that."
- Keep the answer clear and study-guide friendly.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt


# -----------------------------
# Main ask function
# -----------------------------

def ask(question, top_k=5):
    """
    Full RAG pipeline:
    1. Retrieve top-k chunks from ChromaDB.
    2. Build a grounded prompt.
    3. Send prompt to Groq/Llama.
    4. Return answer and sources.
    """

    retrieved_chunks = retrieve(question, top_k=top_k)

    prompt = build_prompt(question, retrieved_chunks)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a grounded study-guide assistant. You must answer only from the provided context."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    # Programmatically collect source names.
    # This guarantees source attribution even if the LLM forgets to cite them.
    sources = []

    for chunk in retrieved_chunks:
        source_label = f"{chunk['source']} — chunk {chunk['chunk_index']}"
        if source_label not in sources:
            sources.append(source_label)

    return {
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": retrieved_chunks
    }


# -----------------------------
# CLI test
# -----------------------------

if __name__ == "__main__":
    test_questions = [
        "What is a normal adult heart rate?",
        "What are the steps for taking blood pressure?",
        "What is the capital of France?"
    ]

    for question in test_questions:
        print("\n" + "=" * 80)
        print(f"QUESTION: {question}")
        print("=" * 80)

        result = ask(question)

        print("\nANSWER:")
        print(result["answer"])

        print("\nSOURCES:")
        for source in result["sources"]:
            print(f"- {source}")