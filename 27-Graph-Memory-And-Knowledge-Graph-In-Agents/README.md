# Module 26: Memory Layer Building (Short, Long, and Semantic Memory)

This module demonstrates how to implement a memory layer for AI agents using **Mem0**. It covers the setup of short-term, long-term, and semantic memory to create more intelligent and context-aware AI applications.

## Key Features

- **Long-Term Memory**: Persistent storage for user preferences and past interactions.
- **Semantic Memory**: Context-aware retrieval of relevant information using embeddings.
- **Gemini Integration**: Utilizing Google's Gemini models for both chat generation and memory extraction.
- **Qdrant Vector Store**: High-performance vector database for storing and searching semantic memories.

## Project Structure

- `memory_agent/`:
    - `mem.py`: The main script implementing the memory-augmented chat agent.
    - `docker-compose.yml`: Docker configuration for spinning up a Qdrant instance.

## Setup & Usage

1. **Start Qdrant**:
   ```bash
   cd memory_agent
   docker-compose up -d
   ```

2. **Configure Environment**:
   Ensure your `.env` file in the root directory contains your `GEMINI_API_KEY`.

3. **Run the Memory Agent**:
   ```bash
   python mem.py
   ```

## How it Works

The agent uses a hybrid approach:
1. **Search**: When a user asks a question, the agent first searches the `mem0` memory store for relevant past interactions.
2. **Context Injection**: Retrieved memories are injected into the system prompt.
3. **Generation**: The AI generates a response using the current query and the retrieved context.
4. **Storage**: The new interaction is automatically added back to the memory store for future use.
