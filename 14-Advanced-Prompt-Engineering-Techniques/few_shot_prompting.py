# Few Shot Prompting

from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)


SYSTEM_PROMPT = """
You are an expert in Coding and only and only answer coding related questions. If user asks anything other than coding related questions, politely refuse to answer.

Rule:
- Strcitly follow the output in JSON format for coding related answers.

Output Format:
{{
  "explanation": "Brief explanation of the code.",
  "code": "The complete code snippet."
}}

Q: Can you explain how to square a + b?
A: Sorry, I can only answer coding related questions.

Q: How do I reverse a string in Python?
A: Sure! Here's a simple way to reverse a string in Python:
...
...
...
```python
def reverse_string(s):
    return s[::-1]
```
Q: Can you code a python program to add two numbers?
A:
```python
def add_numbers(a, b):
    return a + b
```
"""


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you code a python program to multiply two numbers?"}
    ]
)
print(response.choices[0].message.content)

