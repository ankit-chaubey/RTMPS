import asyncio
from rtmps.client import create_client
from rtmps.handlers import register
from rtmps.watcher import watcher
from rtmps.utils import ensure_ffmpeg


async def main():
    # 🔍 Pre-flight check
    ensure_ffmpeg()

    client = await create_client()
    register(client)

    # Background watcher task
    client.loop.create_task(watcher())

    print("🎵 RTMPS running")
    await client.run_until_disconnected()


def run():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 RTMPS stopped by user")
