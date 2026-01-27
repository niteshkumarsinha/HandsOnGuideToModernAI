from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from ollama import Client


app = FastAPI()

client = Client(
    host="http://localhost:11434",
    timeout=30000  # in milliseconds
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.chat(
        model="codellama",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": request.message}
        ]

    )

    return {"response": response.message.content}
        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

