from telethon import TelegramClient
from rtmps.storage import load_config

async def create_client():
    cfg = load_config()
    client = TelegramClient(
        cfg["session"],
        cfg["api_id"],
        cfg["api_hash"]
    )
    await client.start(bot_token=cfg["bot_token"])
    return client
