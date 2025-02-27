import sys
import redis
import functools
from config import CurrentConfig
from app.utils import log_info, log_error

# Load Redis Configurations
REDIS_HOST = CurrentConfig.REDIS_HOST or "localhost"
REDIS_PORT = CurrentConfig.REDIS_PORT or 6379
REDIS_DB = CurrentConfig.REDIS_DB or 0  # Optional: Support multiple databases

@functools.lru_cache(maxsize=1)
def create_redis_client():
    """
    Create a Redis client, establish connection, and return the instance.
    Uses `lru_cache` to ensure only one instance is created per process.
    """
    try:
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            decode_responses=True
        )
        client.ping()  # Test connection
        log_info(f"Connected to Redis successfully at {REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}")
        return client
    except redis.exceptions.ConnectionError as e:
        log_error(f"Failed to connect to Redis at {REDIS_HOST}:{REDIS_PORT} - {e}")
        if __name__ == "__main__":
            sys.exit(1)  # Only exit if running in main process
        return None

def get_redis_client():
    """
    Retrieve the Redis client instance. 
    Ensures a single connection is used throughout the application.
    """
    return create_redis_client()
