# Multi-Modal Agents with LangGraph

This module explores advanced agentic workflows using **LangGraph**, focusing on state management, conditional logic, and persistence.

## Features

- **Stateful Graphs**: Define complex agent logic as a state machine.
- **Conditional Edges**: Route flow based on LLM output or other state values.
- **Persistence (Check-pointing)**: Save and resume agent state using MongoDB.

## Modules & Examples

- **`langgraph/chat.py`**: A basic chatbot implementation using LangGraph.
- **`langgraph/chat_conditional.py`**: Demonstrates conditional routing between different nodes (e.g., repeating a step if the output is insufficient).
- **`langgraph/chat_checkpoint.py`**: Implements persistent memory using `MongoDBSaver`.

## Setup

1.  **MongoDB**: Start the MongoDB instance for checkpointing.
    ```bash
    cd langgraph
    docker-compose up -d
    ```
2.  **Run Example**:
    ```bash
    python langgraph/chat_checkpoint.py
    ```

## Persistence Configuration
The MongoDB checkpointer is configured with a `thread_id`, allowing the agent to remember history across different sessions for the same user or conversation.
