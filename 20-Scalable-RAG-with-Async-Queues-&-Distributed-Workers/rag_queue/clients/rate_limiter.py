import time
from fastapi import HTTPException, Request, status
from .rq_client import redis_client

class RateLimiter:
    def __init__(self, requests: int, window: int):
        self.requests = requests
        self.window = window

    async def __call__(self, request: Request):
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        
        # Use a sliding window or fixed window? 
        # For simplicity, fixed window with a counter
        current = redis_client.get(key)
        
        if current is not None and int(current) >= self.requests:
            ttl = redis_client.ttl(key)
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail={
                    "error": "Rate limit exceeded",
                    "retry_after": ttl if ttl > 0 else self.window
                }
            )
        
        # Increment and set expiry if first request
        pipe = redis_client.pipeline()
        pipe.incr(key)
        pipe.expire(key, self.window)
        pipe.execute()
        
        return True
