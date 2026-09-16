import json 
from app.cache.redis_client import redis_client
from app.config.settings import settings

def get_monitoring_cache(namespace): 
    key = f"k8s:monitoring:{namespace}"
    data = redis_client.get(key)
    if data is None: 
        return None
    return json.loads(data)

def set_monitoring_cache(namespace, data): 
    key = f"k8s:monitoring:{namespace}"
    redis_client.set(key, json.dumps(data, default=str), ex=settings.REDIS_TTL)
    
def delete_monitoring_cache(namespace): 
    key = f"k8s:monitoring:{namespace}"
    redis_client.delete(key)