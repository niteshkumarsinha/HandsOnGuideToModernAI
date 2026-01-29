from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "Generate a caption for this image in about 50 words"},
            {"type": "image_url", "image_url": {"url": "https://images.pexels.com/photos/35748459/pexels-photo-35748459.jpeg"}}
        ]}
    ]
)


print("Response: ", response.choices[0].message.content)