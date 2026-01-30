# Hands-On Guide to Modern AI

This repository contains practical examples and projects for building modern AI applications, ranging from basic Python coding to advanced agentic workflows and scalable RAG systems.

## Modules

### [18. Building AI Agents & Agentic Workflows](./18-Building-AI-Agents-&-Agentic-Workflows/)
Implementation of AI agents using the ReAct (Reasoning and Acting) pattern, featuring tool-use capabilities.

### [19. Building Chat With PDF Project using RAG](./19-Building-Chat-With-PDF-Project-using-RAG/)
A complete pipeline for indexing PDF documents into a Qdrant vector store and performing Retrieval-Augmented Generation (RAG).

### [20. Scalable RAG with Async Queues & Distributed Workers](./20-Scalable-RAG-with-Async-Queues-&-Distributed-Workers/)
An enterprise-grade RAG architecture using FastAPI for the API layer and Redis/RQ for asynchronous task processing.

### [21. Multi-Modal Agents](./21-Multi-Modal-Agents/)
Exploring complex agent structures with LangGraph, including conditional edges and persistent state using MongoDB.

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
