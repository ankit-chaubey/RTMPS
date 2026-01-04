import getpass
from rtmps.storage import save_config

def run():
    print("\n🔧 RTMPS Global Configuration\n")

    api_id = input("API ID: ").strip()
    api_hash = input("API HASH: ").strip()
    bot_token = getpass.getpass("BOT TOKEN (hidden): ").strip()
    session = input("Session name [rtmps]: ").strip() or "rtmps"

    save_config({
        "api_id": int(api_id),
        "api_hash": api_hash,
        "bot_token": bot_token,
        "session": session
    })

    print("\n✅ Configuration saved")
