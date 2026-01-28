from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

# Ensure GEMINI_API_KEY is available for the embedding model
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

pdf_path = Path("/Volumes/Data/Books/Javascript/Learning-JavaScript-3rd-Edition.pdf")
loader = PyPDFLoader(file_path=str(pdf_path))
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = loader.load()
splitted_docs = text_splitter.split_documents(docs)

print(f"Number of chunks to index: {len(splitted_docs)}")

import time

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Initialize vector store with an empty collection or just get reference
# We'll use the constructor to ensure collection exists with correct config
print("Creating/Connecting to collection...")
vector_store = QdrantVectorStore.from_documents(
    documents=splitted_docs[:1], # Start with just one doc to init
    embedding=embedding_model,
    collection_name="learning-javascript",
    url=os.getenv("QDRANT_URL")
)

# Index the rest in batches
batch_size = 20
print(f"Indexing the remaining {len(splitted_docs) - 1} chunks in batches of {batch_size}...")

for i in range(1, len(splitted_docs), batch_size):
    batch = splitted_docs[i : i + batch_size]
    print(f"Indexing batch {i//batch_size + 1}/{(len(splitted_docs)//batch_size) + 1} (Chunks {i} to {min(i + batch_size, len(splitted_docs))})...")
    try:
        vector_store.add_documents(batch)
    except Exception as e:
        print(f"Error in batch {i}: {e}")
        print("Waiting 60 seconds before retrying this batch...")
        time.sleep(60)
        vector_store.add_documents(batch)
    time.sleep(15) # Wait to respect rate limits

print("Indexing of documents completed.")
