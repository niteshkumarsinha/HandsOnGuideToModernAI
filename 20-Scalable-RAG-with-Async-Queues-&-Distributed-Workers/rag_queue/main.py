from rag_queue.server import app
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)