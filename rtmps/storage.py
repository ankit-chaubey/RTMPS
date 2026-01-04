import os
import json

BASE_DIR = os.path.expanduser("~/.rtmps")
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")
CHATS_FILE = os.path.join(BASE_DIR, "chats.json")


def ensure_dir():
    os.makedirs(BASE_DIR, exist_ok=True)


# ---------- GLOBAL CONFIG ----------

def save_config(data):
    ensure_dir()
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_config():
    ensure_dir()
    if not os.path.exists(CONFIG_FILE):
        raise RuntimeError("❌ Run rtmps-config first")
    with open(CONFIG_FILE) as f:
        return json.load(f)


# ---------- CHAT CONFIG ----------

def load_chats():
    ensure_dir()
    if not os.path.exists(CHATS_FILE):
        return {}
    with open(CHATS_FILE) as f:
        return json.load(f)


def save_chats(data):
    ensure_dir()
    with open(CHATS_FILE, "w") as f:
        json.dump(data, f, indent=2)
