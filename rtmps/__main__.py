import asyncio
from rtmps.client import create_client
from rtmps.handlers import register
from rtmps.watcher import watcher

async def main():
    client = await create_client()   # ✅ awaited
    register(client)

    client.loop.create_task(watcher())

    print("🎵 RTMPS running")
    await client.run_until_disconnected()

def run():
    asyncio.run(main())
