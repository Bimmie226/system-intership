import redis
from app.config.settings import settings 

redis_client = redis.Redis(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT, 
    db = settings.REDIS_DB,
    decode_responses=True
)