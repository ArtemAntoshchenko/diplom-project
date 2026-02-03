import redis.asyncio as redis
from ..core.config import settings
from typing import Any, Optional
import pickle

class RedisCache:

    def __init__(self):
        self.client = None
    
    async def connect(self):
        try:
            self.client=redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                password=settings.REDIS_PASSWORD if hasattr(settings, 'REDIS_PASSWORD') else None,
                decode_responses=False,
                socket_keepalive=True
            )
            await self.client.ping()
            print("Redis подключен")
            return True
        except Exception as e:
            print(f"Redis не подключен:{e}. Кэширование отключено.")
            self.client=None
            return False
    
    async def close(self):
        if self.client:
            await self.client.close()
    
    async def get(self, key: str)-> Optional[Any]:
        if not self.client:
            return None
        try:
            data=await self.client.get(key)
            if data:
                return pickle.loads(data)
        except:
            return None
        return None
    
    async def set(self, key: str, value: Any, expire: int=300):
        if not self.client:
            return False
        try:
            serialized=pickle.dumps(value)
            await self.client.setex(key, expire, serialized)
            return True
        except:
            return False
    
    async def delete(self, key: str):
        if not self.client:
            return False
        try:
            await self.client.delete(key)
            return True
        except:
            return False
    
    async def clear_pattern(self, pattern: str="*"):
        if not self.client:
            return False
        try:
            keys=await self.client.keys(pattern)
            if keys:
                await self.client.delete(*keys)
            return True
        except:
            return False
        
cache=RedisCache()