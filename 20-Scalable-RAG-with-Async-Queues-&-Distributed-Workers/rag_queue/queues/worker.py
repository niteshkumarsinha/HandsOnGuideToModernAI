import os
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"

from openai import OpenAI
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

gemini_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
) 

vector_db = None

def get_vector_db():
    global vector_db
    if vector_db is None:
        vector_db = QdrantVectorStore.from_existing_collection(
            collection_name="learning-javascript",
            url=os.getenv("QDRANT_URL"),
            embedding=embedding_model
        )
    return vector_db

def process_queries(query: str):
    print(f"Processing query: {query}")
    db = get_vector_db()
    search_results = db.similarity_search(query)
    print(f"Search results: {search_results}") 
    context = "\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page']}\nPage Label: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}\n" for result in search_results]) 
    
    SYSTEM_PROMPT = f"""
                        You are a helpful assistant that can answer questions about the book 'Learning JavaScript'. You are also a teacher and can explain the concepts in a simple way. If you don't know the answer, you should say so.

                        You should only answer the question based on the context provided. If the question is not related to the context, you should say so.

                        Context: {context}  """

    response = gemini_client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )
    
    return response.choices[0].message.content


    
