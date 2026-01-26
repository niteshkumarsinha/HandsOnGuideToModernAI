from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

g_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = g_client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in simple terms."
)

print(response.text)
