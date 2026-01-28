from fastapi import FastAPI, Query
from rag_queue.clients.rq_client import queue
from rag_queue.queues.worker import process_queries
from rag_queue.clients.rate_limiter import RateLimiter
from fastapi import Depends


app = FastAPI()

# Limit: 2 requests per 60 seconds
chat_limiter = RateLimiter(requests=2, window=60)

@app.get("/")
def root():
    return {"message": "Server is up and running"}

@app.post("/chat", dependencies=[Depends(chat_limiter)])
def chat(
    query: str = Query(..., description="The chat query for the assistant")
):
    job = queue.enqueue(process_queries, query)
    return {"job_id": job.id, "status": "queued"}

@app.get("/status/{job_id}")
def check_status(job_id: str):
    from rq.job import Job
    from rag_queue.clients.rq_client import redis_client
    job = Job.fetch(job_id, connection=redis_client)
    
    if job.is_finished:
        return {"status": "finished", "result": job.result}
    elif job.is_failed:
        return {"status": "failed", "error": str(job.exc_info)}
    else:
        return {"status": job.get_status()}