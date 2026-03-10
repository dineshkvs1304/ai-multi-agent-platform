import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


def get_cache(key):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def set_cache(key, value):
    redis_client.set(key, json.dumps(value), ex=3600)