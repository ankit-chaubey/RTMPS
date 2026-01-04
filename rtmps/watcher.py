import asyncio
from rtmps.player import PLAYERS
from rtmps.ffmpeg import start

async def watcher():
    while True:
        await asyncio.sleep(1)
        for p in PLAYERS.values():
            if p.process and p.process.poll() is not None:
                if p.loop > 0:
                    p.loop -= 1
                    p.process = start(p.chat_id, p.current_file)
                    continue

                p.process = None
                p.current_file = None
                p.current_msg = None

                if p.next_file:
                    p.process = start(p.chat_id, p.next_file)
                    p.current_file = p.next_file
                    p.current_msg = p.next_msg
                    p.next_file = None
                    p.next_msg = None
