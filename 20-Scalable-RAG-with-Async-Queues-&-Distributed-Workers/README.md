# Scalable RAG with Async Queues & Distributed Workers

This module demonstrates a production-ready, scalable architecture for RAG systems using asynchronous task processing.

## Architecture

1.  **API Layer (FastAPI)**: Receives user queries and enqueues them for processing.
2.  **Task Queue (Redis/RQ)**: Manages the distribution of tasks.
3.  **Worker Layer**: Distributed workers that pick up jobs from the queue, perform RAG, and store results.
4.  **Rate Limiter**: Built-in rate limiting to prevent API abuse.

## Folder Structure

- `rag_queue/server.py`: FastAPI server implementation.
- `rag_queue/queues/worker.py`: Worker logic for processing RAG tasks.
- `rag_queue/clients/`: Redis and RQ client configurations.
- `docker-compose.yml`: Configuration for running Redis.

## Running the System

1.  **Start Redis**:
    ```bash
    docker-compose up -d
    ```

2.  **Start the Worker**:
    ```bash
    # From the module root
    rq worker --path .
    ```

3.  **Start the Server**:
    ```bash
    uvicorn rag_queue.server:app --reload
    ```

### API Endpoints
- `POST /chat?query=...`: Submit a query (returns `job_id`).
- `GET /status/{job_id}`: Check the status and retrieve the result of a job.
