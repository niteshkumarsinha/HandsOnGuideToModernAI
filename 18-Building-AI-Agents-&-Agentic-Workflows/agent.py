from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import subprocess
from pydantic import BaseModel, Field
from typing import Optional, List

load_dotenv()

MODEL_ID = "gemini-2.5-flash"

def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t+%w"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"The weather in {city} is {response.text}"
        return f"Error: Received status code {response.status_code} for {city}"
    except Exception as e:
        return f"Error: Could not retrieve weather for {city}: {str(e)}"

def run_command(command):
    try:
        # Use shell=True for complex commands, capture output and error
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout.strip()
        error = result.stderr.strip()
        if error:
            return f"Output: {output}\nError: {error}"
        return output if output else "Command executed successfully (no output)."
    except Exception as e:
        return f"Error executing command: {str(e)}"

# Tool registry
tools = {
    "get_weather": get_weather,
    "run_command": run_command
}

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The type of step. Valid values: PLAN, TOOL, OUTPUT")
    content: Optional[str] = Field(None, description="The reasoning content or final answer.")
    tool: Optional[str] = Field(None, description="The tool to call (if step is TOOL).")
    input: Optional[str] = Field(None, description="The exact input string for the tool (if step is TOOL).")

SYSTEM_PROMPT = """
You are a helpful assistant that solves queries using a Chain of Thought (ReAct) pattern.
You must use the provided JSON format for every response.

Available tools:
- get_weather(city): Returns weather string for a city.
- run_command(command): Executes a shell command and returns output.

Workflow:
1. PLAN: Analyze the user query and decide on the next step.
2. TOOL: Call a tool if information or action is needed. Provide 'tool' name and 'input' (as a string).
3. OBSERVE: You will receive the tool's output as an 'Observation'. (Handled by the system)
4. OUTPUT: Once you have enough information, provide the final answer in 'content'.

Rules:
- Always reason step-by-step.
- Only call one tool at a time.
- If you call a tool, wait for the observation before continuing.
"""

def run_agent(query):
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta"
    )   
    
    # Message history is critical for ReAct
    history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query}
    ]
    
    print(f"--- Starting Agent for Query: {query} ---")
    
    for i in range(10):  # Limit iterations
        try:
            chat = client.beta.chat.completions.parse(
                model=MODEL_ID,
                messages=history,
                response_format=MyOutputFormat
            )
            
            # Access the parsed object directly
            parsed = chat.choices[0].message.parsed
            history.append({"role": "assistant", "content": chat.choices[0].message.content})
            
            print(f"\nStep {i+1} [{parsed.step}]: {parsed.content or ''}")
            
            if parsed.step == "OUTPUT":
                print(f"\nFINAL ANSWER: {parsed.content}")
                break
            
            if parsed.step == "TOOL" and parsed.tool:
                tool_name = parsed.tool
                tool_input = parsed.input
                
                print(f"Calling Tool: {tool_name}({tool_input})")
                
                if tool_name in tools:
                    observation = tools[tool_name](tool_input)
                else:
                    observation = f"Error: Tool '{tool_name}' not found."
                
                print(f"Observation: {observation}")
                history.append({"role": "user", "content": f"Observation: {observation}"})
            
            elif parsed.step == "PLAN":
                # If it's just a plan, it should probably be followed by a TOOL or OUTPUT in the next turn
                # We don't need to do anything here except continue the loop
                pass
                
        except Exception as e:
            print(f"Error during agent execution: {e}")
            break
    else:
        print("\nAgent reached maximum iterations without a final answer.")

if __name__ == "__main__":
    # Test multiple tools and multi-step reasoning
    #run_agent("What is the weather like in Dhanbad, Delhi, Mumbai?")
    #print("\n" + "="*50 + "\n")
    run_agent("List files in the current directory and count them.")