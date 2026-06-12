# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
     I chose a Medical Assistant Study Guide Chatbot. As a Medical Assistant, there is a lot of information that you're supposed to be aware of in order to gain your license. This information can stretch from medical terminology to how to interpret an EKG. Oftentimes I was surrounded by 5 different books and wanted to streamline the process by creating a chatbot that has all the information one needs to study. Instead of having a billion tabs or textbooks open, you can ahve one tab open with all the information you need.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description                                  | URL or location |
|---|--------|----------------------------------------------|-----------------|
| 1 | | | |    Vital Signs: blood pressure, purlse rate, etc  
https://www.hopkinsmedicine.org/health/conditions-and-diseases/vital-signs-body-temperature-pulse-rate-respiration-rate-blood-pressure 

| 2 | | | |   Common Medical Terms                          https://www.rcog.org.uk/for-the-public/a-z-of-medical-terms/ 

| 3 | | | |   Anatomy and Physiology                        https://www.cliffsnotes.com/study-guides/anatomy-and-physiology 

| 4 | | | |   Common Medical Abbreviations                  
https://www.asha.org/practice-portal/professional-issues/documentation-in-health-care/common-medical-abbreviations/?srsltid=AfmBOor_F8eVZTVh6MNF_-8R9-aPP78Ms8feFN0Zy96HDKYZEZDVmXIa 

| 5 | | | |  OSHA Healthcare Standards                      https://www.cdc.gov/niosh/learning/safetyculturehc/module-5/5.html 

| 6 | | | |  HIPPA Training Requirements                    https://www.hipaajournal.com/hipaa-training-requirements/ 

| 7 | | | |  Phlebotomy Guide                               https://phlebotomyusa.com/blog/phlebotomy/a-step-by-step-guide-to-phlebotomy-procedure/ 

| 8 | | | |  EKG Basics                                     https://www.aclsmedicaltraining.com/basics-of-ecg 

| 9 | | | |  Common Lab Procedure & Their Meaning           https://www.parentprojectmd.org/wp-content/uploads/2021/02/Common_Labs.pdf 

| 10 | | | | Beside Manner & Patient Interaction            https://med.stanford.edu/stanfordmedicine25/blog/archive/20240/bedside-communication-tips.html 

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
chunk size = 500 characters

**Overlap:**
chunk overlap = 100 characters
**Reasoning:**
This is just the iniitial split. Im nto sure if this would be best for my system but once its been tested and quiered differently, ill be able to determine if this is the best fit 
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 via sentence-transformers

**Top-k:**
3 because you dont want to overload the LLM will a lot of resources and create unnessary noise and jitter. Retrieving the three most relevant chunks would provide sufficient context to the LLM. 

**Production tradeoff reflection:**
I would prefer a model trained on medical text since im making a medical assistant chatbox. It would also be cool to have multilingual support. 
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question                                       | Expected answer |
|---|------------------------------------------------|-----------------|
| 1 | What does HIPPA stand for?                      Health Insurance Portability and Accountability Act
| 2 | What are the steps for taking blood pressure?   A multi-step answer 
| 3 | What is a normal adult heart rate?              a normal resting adult heart rate typically ranges from 60-100 beats per minute
| 4 | What is hypertension?                           hypertension is a condition in which blood pressure remains consistently higher than normal levels 
| 5 | What is the purpose of HIPPA?                   HIPPA protects patient privacy and ensures the secure handling of health information

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. My chunks and overlap may be wrong. the test questions will help determine

2. having the right about of retrieval chunks. if its too low, the bot may miss relevant information. if its too many it may introduce unrelated context and confuse the model

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->


Medical Assistant Study Guide Websites
        ↓
[1] Document Ingestion
Tool: PyPDFLoader 
Purpose: Load the 10 medical assistant reference documents into the project
        ↓
[2] Chunking
Tool: RecursiveCharacterTextSplitter
Purpose: Split documents into smaller chunks using a set chunk size and overlap
        ↓
[3] Embedding + Vector Store
Tool: all-MiniLM-L6-v2 via sentence-transformers + ChromaDB
Purpose: Convert chunks into embeddings and store them in a searchable vector database
        ↓
[4] Retrieval
Tool: ChromaDB similarity search
Purpose: Retrieve the top-k most relevant chunks based on the user’s question
        ↓
[5] Generation
Tool: Llama 3.3 70B through Groq API
Purpose: Generate a natural-language answer using the retrieved context
        ↓
Final Chatbot Response
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

     Document Ingestion
     ChatGPT to generate code that loads my medical assistant PDF and text documents into the application and verify that all documents are successfully imported.

     Chunking
     ChatGPT to implement document chunking using my selected chunk size and overlap and verify that important medical concepts remain intact.

     Embedding + Vector Store
     ChatGPT to create embeddings with all-MiniLM-L6-v2 and store them in ChromaDB, then verify that all chunks are indexed correctly.

     Retrieval
     ChatGPT to implement top-k retrieval and verify that relevant chunks are returned for my test questions.

     Generation
     ChatGPT to integrate Groq and Llama 3.3 for response generation and verify that answers are accurate and grounded in the retrieved context.

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
