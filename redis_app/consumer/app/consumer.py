import asyncio
from redis import asyncio as aioredis
from app.config import settings


async def consume():
    redis = await aioredis.from_url(settings.redis_url)
    pubsub = redis.pubsub()
    channel_name = "test_channel"
    
    # Подписываемся на канал
    await pubsub.subscribe(channel_name)

    try:
        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True)
            if message:
                print(f"Received: {message['data'].decode('utf-8')}")
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        await pubsub.unsubscribe(channel_name)
        print("Unsubscribed and exiting...")

