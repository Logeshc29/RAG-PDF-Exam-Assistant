# Architecture

Student
    ↓
Upload PDF
    ↓
PDF Loader
    ↓
Text Chunking
    ↓
Embeddings
(HuggingFace)
    ↓
FAISS Vector Store
    ↓
Question Asked
    ↓
Context Retrieval
    ↓
LLM
    ↓
Answer
