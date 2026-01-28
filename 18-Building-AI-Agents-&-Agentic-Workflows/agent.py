from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
from pydantic import BaseModel, Field
from typing import Optional


load_dotenv()

MODEL_ID = "gemini-2.5-flash"

def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t+%w"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Sorry, I couldn't get the weather for that city."


# Tool registry
tools = {
    "get_weather": get_weather
}

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The id of the step. Example: PLAN, OBSERVE, TOOL, OUTPUT, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step.")
    tool: Optional[str] = Field(None, description="The tool to use.")
    input: Optional[str] = Field(None, description="The input params for the tool")

SYSTEM_PROMPT = """
You are a helpful assistant that can use tools to resolve user queries using chain of thought.
Output JSON format:
{"step": "PLAN/OBSERVE/OUTPUT", "content": "Your content here.", "tool": "The tool to use.", "input": "The input params for the tool"}    

Available tools:
- get_weather(city): Returns the weather in the given city.

Follow this thought process:
Thought: Reason about the problem and what tool you need.
Action: tool_name(arg1)

Follow PLAN, OBSERVE and FINAL ANSWER steps.

Observation: The result from the tool.
... (repeat)
Final Answer: The final result.

Example:
Thought: I need to get the weather in New York.
Action: get_weather("New York")
Observation: The weather in New York is sunny and 70 degrees.
Final Answer: The weather in New York is sunny and 70 degrees.  
"""

def run_agent(query):
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta"
    )   
    chat = client.chat.completions.parse(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ],
        response_format=MyOutputFormat
    )
    
    # Send system prompt and query combined
    print(f"User Query: {query}\n")
    
    # First message: System Prompt + Query
    current_prompt = "\n\nUser Query: " + query
    
    for _ in range(5):  # Limit steps
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": current_prompt}
            ]
        )
        content = response.choices[0].message.content
        print(content)
        
        if "Final Answer:" in content:
            break
            
        if "Action:" in content:
            try:
                action_line = [line for line in content.split("\n") if "Action:" in line][0]
                action_part = action_line.split("Action:")[1].strip()
                func_name = action_part.split("(")[0]
                args_str = action_part.split("(")[1].split(")")[0]
                args = [int(x.strip()) for x in args_str.split(",")]
                
                if func_name in tools:
                    result = tools[func_name](*args)
                    print(f"Observation: {result}")
                    current_prompt = f"Observation: {result}"
                else:
                    current_prompt = f"Observation: Tool {func_name} not found."
            except Exception as e:
                current_prompt = f"Observation: Error parsing action: {e}"
        else:
            # If no action or final answer, just wait (shouldn't happen with good CoT)
            break

if __name__ == "__main__":
    query = "What is the weather like in Dhanbad, Delhi, Mumbai"
    run_agent(query)