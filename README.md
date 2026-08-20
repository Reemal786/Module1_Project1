# 🩺 MedQuery — Medical Assistant Study Assistant

**MedQuery** is an AI-powered study assistant designed to help students preparing for Medical Assistant certification exams quickly find reliable answers from their study materials.

Instead of searching through multiple documents manually, users can ask questions in natural language and receive answers generated from a curated collection of medical reference materials.

MedQuery uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information before generating a response, helping keep answers grounded in the provided sources.

## 🎯 Purpose

Medical Assistant students often study from information spread across textbooks, PDFs, online resources, and study guides. Finding a specific answer can require searching through multiple sources.

MedQuery explores how **RAG and semantic search** can make those materials easier to navigate by providing a single interface where students can ask questions and retrieve relevant information from their study resources.

The project also demonstrates how LLMs can be combined with external knowledge bases to create AI applications that are more **grounded and transparent** than relying on an LLM alone.

## ✨ Features

* **Natural Language Q&A** — Ask medical assistant study questions conversationally
* **Document Retrieval** — Searches indexed study materials for information relevant to each question
* **RAG Pipeline** — Combines semantic retrieval with an LLM to generate context-aware answers
* **Semantic Search** — Uses vector embeddings to retrieve information based on meaning rather than exact keywords
* **Source Attribution** — Provides sources alongside generated responses
* **Interactive Interface** — Simple Gradio interface for submitting questions and viewing responses
* **Knowledge Base** — Processes information from multiple medical reference documents

## 🧠 How It Works

```text
                User Question
                      │
                      ▼
             SentenceTransformer
                      │
                      ▼
               Query Embedding
                      │
                      ▼
                  ChromaDB
                      │
                      ▼
          Relevant Document Chunks
                      │
                      ▼
              Llama 3.3 70B
                      │
                      ▼
         Grounded Answer + Sources
```

### 1. Document Processing

Medical reference materials are collected and divided into smaller text chunks that can be efficiently searched.

### 2. Embedding Generation

MedQuery uses **SentenceTransformers (`all-MiniLM-L6-v2`)** to convert the document chunks into numerical vector embeddings that capture their semantic meaning.

### 3. Vector Storage

The embeddings and their corresponding text are stored in **ChromaDB**, allowing the application to perform semantic similarity searches.

### 4. Retrieval

When a user asks a question, the question is embedded using the same SentenceTransformer model. ChromaDB searches the knowledge base and retrieves the document chunks most relevant to the query.

### 5. Response Generation

The retrieved context and the user's question are sent to **Llama 3.3 70B** through the Groq API. The model is instructed to generate its response using the retrieved material rather than relying solely on its internal knowledge.

### 6. Source Attribution

Relevant sources are displayed with the generated response so users can reference the original study material.

## 🛠️ Tech Stack

**Language**

* Python

**AI & Machine Learning**

* Retrieval-Augmented Generation (RAG)
* Llama 3.3 70B
* SentenceTransformers
* `all-MiniLM-L6-v2`
* Semantic Search

**Database**

* ChromaDB

**API**

* Groq API

**Interface**

* Gradio

## 📚 Knowledge Base

MedQuery processes medical study materials from multiple PDFs and web-based resources.

The documents are:

1. Extracted and cleaned
2. Divided into smaller chunks
3. Converted into vector embeddings
4. Stored in ChromaDB
5. Retrieved based on their semantic similarity to a user's question

The resulting knowledge base contains **500+ searchable document chunks**.

## ⚠️ Disclaimer

MedQuery is intended as an **educational and study tool**. It is not designed to provide medical diagnoses, treatment recommendations, or professional medical advice.

## 🔮 Future Improvements

* Expand the medical knowledge base
* Improve retrieval and response evaluation
* Add conversation history
* Allow users to upload their own study materials
* Add filtering by source or medical topic
* Develop practice quizzes from retrieved material
* Add user accounts and study progress tracking

## 👩‍💻 Author

**Reemal Hoor**
Computer Engineering
