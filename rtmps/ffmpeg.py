import subprocess
from rtmps.storage import load_chats

def start(chat_id, file):
    chats = load_chats()
    cfg = chats[str(chat_id)]
    return subprocess.Popen([
        "ffmpeg", "-re",
        "-i", file,
        "-vn",
        "-c:a", "copy",
        "-f", "flv",
        cfg["rtmps_url"] + cfg["rtmps_key"]
    ])
