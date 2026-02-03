from aiohttp import ClientSession
from fastapi import Depends
from ..core.config import settings
from .redis import cache


class WeatherClient():
    def __init__(self, base_url:str):
        self.base_url=base_url
        
    async def get_info(self, profile_data):
        cache_key=f'weather:{profile_data.city}'
        cached=await cache.get(cache_key)
        if cached:
            return cached
        async with ClientSession(base_url=self.base_url) as session:
            async with session.get(f'/data/2.5/forecast?q={profile_data.city}&units=metric&appid={settings.API_KEY}') as respons:
                result=await respons.json()
                await cache.set(cache_key, result, expire=3600)
                return result
