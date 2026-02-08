#from dotenv import load_dotenv
import os
load_dotenv()

from langgraph.graph import StateGraph, START, END   
from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta",   
)

class State(TypedDict):
    user_query: str 
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": state["user_query"]}
        ]
    )
    return {"llm_output": response.choices[0].message.content}

def evaluate_response(state: State) -> Literal["chatbot_gemini", END]:
    # Simplified evaluation logic
    if state.get("llm_output"):   
        return END
    return "chatbot_gemini"  

def chatbot_gemini(state: State):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",   
        messages=[
            {"role": "user", "content": state["user_query"]}
        ]
    )
    return {"llm_output": response.choices[0].message.content}


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_edge("chatbot_gemini", END)

graph = graph_builder.compile()
updated_state = graph.invoke({"user_query": "What is 2 + 2?"})    

print(updated_state["llm_output"])
