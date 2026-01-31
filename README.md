# Hands-On Guide to Modern AI

This repository contains practical examples and projects for building modern AI applications, ranging from basic Python coding to advanced agentic workflows and scalable RAG systems.

## Modules

### [1. Intro to Coding with Python](./1-IntroToCodingWithPython/)
Basics of Python programming, including variables, functions, and control flow.

### [2. Data Types in Python](./2-Data-Types-In-Python/)
In-depth look at Python objects, mutability, and core data types.

### [13. Core Foundations of Generative AI](./13-Core-Foundations-GenerativeAI/)
Fundamental concepts of LLMs, tokenization, and basic model interactions.

### [14. Advanced Prompt Engineering Techniques](./14-Advanced-Prompt-Engineering-Techniques/)
Techniques like Chain-of-Thought (CoT), Few-Shot Prompting, and Persona-based prompting.

### [15. Prompt Serialization & Instruction Formats](./15-Prompt-Serialization-&-Instruction-Formats/)
Best practices for structuring prompts and instructions for LLMs.

### [16. Local LLM Deployment & API Integration](./16-Local-LLM-Deployment-&-API-Integration/)
Running models locally and integrating them into applications via APIs.

### [17. Running LLMs via Hugging Face](./17-RunningLLMs-via-HuggingFace/)
Utilizing the Hugging Face Transformers library to run and experiment with open-source models.

### [18. Building AI Agents & Agentic Workflows](./18-Building-AI-Agents-&-Agentic-Workflows/)
Implementation of AI agents using the ReAct (Reasoning and Acting) pattern, featuring tool-use capabilities.

### [19. Building Chat With PDF Project using RAG](./19-Building-Chat-With-PDF-Project-using-RAG/)
A complete pipeline for indexing PDF documents into a Qdrant vector store and performing Retrieval-Augmented Generation (RAG).

### [20. Scalable RAG with Async Queues & Distributed Workers](./20-Scalable-RAG-with-Async-Queues-&-Distributed-Workers/)
An enterprise-grade RAG architecture using FastAPI for the API layer and Redis/RQ for asynchronous task processing.

### [21. Multi-Modal Agents](./21-Multi-Modal-Agents/)
Exploring complex agent structures with LangGraph, including conditional edges and persistent state using MongoDB.

### [26. Memory Layer Building (Short, Long, & Semantic Memory)](./26-Memory-Layer-Building-Short-Long-And-Semantic-Memory-In-AI/)
Implementation of an advanced memory layer using Mem0, featuring persistent chat history and context-aware retrieval.

### [27. Graph Memory & Knowledge Graph in Agents](./27-Graph-Memory-And-Knowledge-Graph-In-Agents/)
Integrating Knowledge Graphs (Neo4j) with long-term memory for enhanced agent reasoning.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/niteshkumarsinha/HandsOnGuideToModernAI.git
   cd HandsOnGuideToModernAI
   ```

2. **Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_api_key
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## License
MIT
