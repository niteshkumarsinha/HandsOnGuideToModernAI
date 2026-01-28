from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



pdf_path = Path("/Volumes/Data/Books/Javascript/Learning-JavaScript-3rd-Edition.pdf")
loader = PyPDFLoader(file_path=pdf_path)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = loader.load()
splitted_docs = text_splitter.split_documents(docs)
print(len(docs))
print(len(splitted_docs))