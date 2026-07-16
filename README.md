# RAG PDF Exam Assistant

## Overview

An AI-powered exam preparation assistant that allows students to upload PDFs, generate summaries, and ask questions from study material.

## Features

- Upload PDF Notes
- Generate Summaries
- Ask Questions from PDF
- Important Question Generation
- MCQ Generation
- Flashcard Generation
- Retrieval-Augmented Generation (RAG)

## Architecture

Architecture.png

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace
- SentenceTransformers

## Workflow

1. Upload PDF
2. Extract Text
3. Chunk Content
4. Generate Embeddings
5. Store in FAISS
6. User Asks Questions
7. Retrieve Relevant Context
8. LLM Generates Answer
