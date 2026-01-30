# Building AI Agents & Agentic Workflows

This module demonstrates the implementation of AI agents using the **ReAct** (Reasoning and Acting) pattern. The agent can plan its actions, use tools, and process observations to reach a final answer.

## Features

- **ReAct Pattern**: Implements a structured loop of planning, tool execution, and observation.
- **Tool Integration**: Includes tools for retrieving weather information and executing shell commands.
- **Pydantic Validation**: Uses Pydantic for structured LLM output parsing.

## Files

- `agent.py`: The main agent implementation using the Gemini API.
- `main.py`: Entry point for running agent experiments.

## Tools

1.  **`get_weather(city)`**: Fetches weather data from `wttr.in`.
2.  **`run_command(command)`**: Safely executes shell commands and returns the output/error.

## Getting Started

Ensure your `.env` file has the `GEMINI_API_KEY` set.

Run the agent:
```bash
python agent.py
```

### Example Usage
The agent is configured to handle queries like:
- "What is the weather like in New York?"
- "List files in the current directory and count them."
