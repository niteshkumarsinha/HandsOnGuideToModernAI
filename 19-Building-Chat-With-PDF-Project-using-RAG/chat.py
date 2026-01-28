from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")  


gemini_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)  

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)   

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="learning-javascript",
    url=os.getenv("QDRANT_URL"),
)

# Take user input
user_query = input("Ask Something: ")
search_results = vector_db.similarity_search(user_query)

context = "\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page']}\nPage Label: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}\n" for result in search_results]) 

SYSTEM_PROMPT = f"""
You are a helpful assistant that can answer questions about the book 'Learning JavaScript'. You are also a teacher and can explain the concepts in a simple way. If you don't know the answer, you should say so.

You should only answer the question based on the context provided. If the question is not related to the context, you should say so.

Context: {context}  
"""


response = gemini_client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)   



print("\nSearch Results:")
for result in search_results:
    print(result.page_content)

print("\nResponse:")
print(response.choices[0].message.content)
    