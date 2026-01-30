from dotenv import load_dotenv  
import os

from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.mongodb import MongoDBSaver  

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": response}



graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()


def compile_graph_with_checkpoint(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

    

DB_URI = "mongodb://langgraph_user:langgraph_password@localhost:27017"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:  
    graph_with_checkpointer = compile_graph_with_checkpoint(checkpointer)

    config = {
        "configurable": {
            "thread_id": "1"
        }
    }

    # updated_state = graph_with_checkpointer.invoke(State({"messages": ["What is my name"]}), config,)

    # print(updated_state)    

    for event in graph_with_checkpointer.stream(State({"messages": ["What am I learning"]}), config, stream_mode="values"):  
        event["messages"][-1].pretty_print()
