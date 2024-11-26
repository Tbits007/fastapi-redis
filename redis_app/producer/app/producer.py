from redis import asyncio as aioredis
from app.config import settings


async def produce(channel_name, message):
    redis = await aioredis.from_url(settings.redis_url)
    
    await redis.publish(channel_name, message)
    print(f"Published: {message}")