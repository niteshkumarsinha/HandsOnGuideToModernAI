# Building Chat With PDF Project using RAG

This module provides a complete pipeline for building a Retrieval-Augmented Generation (RAG) system that can answer questions based on a PDF document.

## Architecture

- **Loader**: Uses `PyPDFLoader` to extract text from PDFs.
- **Text Splitter**: Uses `RecursiveCharacterTextSplitter` to create manageable chunks.
- **Embeddings**: Uses `GoogleGenerativeAIEmbeddings` (Gemini) for vector representations.
- **Vector Store**: Uses **Qdrant** for efficient similarity search.

## Files

- `index.py`: Script to load, split, and index a PDF into Qdrant.
- `chat.py`: Interactive script to query the RAG system.
- `docker-compose.yml`: (Optional) Setup for local Qdrant instance.

## Setup & Indexing

1.  **PDF Path**: Update the `pdf_path` in `index.py` to point to your PDF file.
2.  **Vector Store**: Ensure Qdrant is running (either locally or via Qdrant Cloud).
3.  **Run Indexing**:
    ```bash
    python index.py
    ```
    This script indexes the document in batches to respect API rate limits.

4.  **Chat with PDF**:
    ```bash
    python chat.py
    ```
