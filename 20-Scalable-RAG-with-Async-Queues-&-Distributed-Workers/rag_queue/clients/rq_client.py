from redis import Redis
from rq import Queue
from dotenv import load_dotenv
import os

load_dotenv()

redis_client = Redis(host="localhost", port=6379, db=0)
queue = Queue(connection=redis_client)


