from mem0 import Memory
import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
NEO4J_URL = os.getenv("NEO4J_URL")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))

config = {
    "version": "v1.1",   
    "embedder": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "models/text-embedding-004",
        }
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "gemini-2.0-flash",
        }
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": NEO4J_URL,
            "username": NEO4J_USERNAME,
            "password": NEO4J_PASSWORD
        }   
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": QDRANT_HOST,
            "port": QDRANT_PORT,
            "collection_name": "mem0_gemini_final",
            "embedding_model_dims": 768,
        }
    }
}



memory_client = Memory.from_config(config)


from google import genai

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)   

while True:

    user_query = input("> ")

    search_memory = memory_client.search(
        user_id="user123",
        query=user_query,
        limit=5
    )

    memories = [
        f"ID: {mem.get("id")}\nMemory: {mem.get("memory")}\n" for mem in search_memory.get("results")
    ]

    print("Found Memories: ", memories)

    SYSTEM_PROMPT = f"""
    You are a helpful assistant.
    Use the following memories to answer the user's query.
    If the answer is not in the memories, say so.
    
    Memories:
    {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content

    print("AI: ", ai_response)

    memory_client.add(
        user_id="user123",  
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

    print("Memory added successfully")
