from dotenv import load_dotenv
from openai import OpenAI
import os
import json
        
load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)


SYSTEM_PROMPT = """
You are an expert in Resolving User Queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The Plan can be multiple steps.
Once you think enough PLAN has been made, you will OUTPUT the final answer.

Rules:
- Always think step by step.
- Always separate PLAN and OUTPUT clearly.
- Strcitly follow the output in JSON format.
- The sequence is START (user query) -> PLAN (your plan) -> OUTPUT (final answer).


Output JSON Format:
{"step": "START/PLAN/OUTPUT", "content": "Your content here."}

Example:
Q: Hey, Can you solve 2 + 3 * 5 / 10
A:
{"step": "START", "content": "User asked to solve the expression 2 + 3 * 5 / 10."}
{"step": "PLAN", "content": "Looking at the problem, The BODMAS rule should be followed in the calculations."}
{"step": "PLAN", "content": "1. First, calculate the multiplication: 3 * 5 = 15. 2. Next, calculate the division: 15 / 10 = 1.5. 3. Finally, add the result to 2: 2 + 1.5 = 3.5."}
{"step": "OUTPUT", "content": "The final answer is 3.5."}

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, Can you solve 4 + 6 / 2 - 3"}
    ]
)
print(response.choices[0].message.content)


print("\n\n--- Interactive Mode ---\n\n")
message_history = []
system_prompt =  {"role": "system", "content": SYSTEM_PROMPT},
message_history.append(system_prompt)

user_query = input("$-> ")
message_history.append({"role": "user", "content": user_query})


while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )
    # Extract and validate the response content
    raw_content = response.choices[0].message.content
    parsed_content = dict[str, str]()
    if raw_content:
        try:
            # Attempt to parse the content as JSON
            parsed_content: dict[str, str] = json.loads(raw_content)
            message_history.append({"role": "assistant", "content": raw_content})
            print(parsed_content)
        except json.JSONDecodeError as e:
            print("Failed to parse the response content as JSON. Error:", e)
            print("Raw content received:", raw_content)
    else:
        print("No content received in the response.")

    if parsed_content.get("step") == "START":
        print(f"Starting : {parsed_content['content']}")
    elif parsed_content.get("step") == "PLAN":
        print(f"Planning : {parsed_content['content']}")
    elif parsed_content.get("step") == "OUTPUT":
        print(f"Output : {parsed_content['content']}")
        break
    else:
        print(f"{parsed_content['step']}: {parsed_content['content']}") 

print("\n--- Done ---\n")

