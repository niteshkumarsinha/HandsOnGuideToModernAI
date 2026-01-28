from openai import OpenAI
from dotenv import load_dotenv
import os
import requests


load_dotenv()

def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t+%w"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Sorry, I couldn't get the weather for that city."

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
) 

def main():
    user_query = "What is the weather like in " + input("Enter your city: ")
    city = user_query.split("in ")[-1]
    weather = get_weather(city)
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_query}\n{weather}"}
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()

