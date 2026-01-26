import os
from openai import OpenAI
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hey There!"}
    ]
)

print(response.choices[0].message.content)