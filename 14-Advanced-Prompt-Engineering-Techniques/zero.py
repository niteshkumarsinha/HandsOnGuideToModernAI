# Zero shot prompting 

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

# Zero shot prompting : Directly instructing the model to perform a task without any prior examples.
SYSTEM__PROMPT = "You are an expert in Coding and only and only answer coding related questions. If user asks anything other than coding related questions, politely refuse to answer."


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM__PROMPT},
        {"role": "user", "content": "Can you code a python program to add two numbers?"}
    ]
)

print(response.choices[0].message.content)