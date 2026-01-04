# RTMPS

RTMPS is a high-performance **Telegram Voice Chat music streaming engine** built using **Telethon** and **FFmpeg**, designed specifically for **RTMPS-based voice chats**.

It supports **multiple Telegram groups simultaneously**, each with its own **RTMPS stream, queue, and FFmpeg process**, while preserving a clean and informative user experience.

---

## ✨ Features

- 🎧 Stream music to Telegram Voice Chats via RTMPS
- 🧩 Multi-group support
  - Different chats
  - Different songs
  - Different queues
  - Different FFmpeg processes
- 🔐 Secure global configuration via CLI
- ⚙️ Per-chat RTMPS setup using `/setup`
- 📥 Smart queue management with preloading
- 🔁 Loop, shuffle, skip, clear queue
- 🕊️ Informative status messages (Downloading…, Added to queue, etc.)
- 🚀 Built as a real PyPI package, not a raw script

---

## 📦 Installation

```bash
pip install rtmps
```

> ⚠️ FFmpeg is required and must be available in your system PATH.




---

## 🔧 Global Configuration (One-Time)

Run the configuration wizard:

`rtmps-config`

You will be asked for:

`API_ID`

`API_HASH`

`BOT_TOKEN`

Session name (optional)


Configuration is stored at:

`~/.rtmps/config.json`


---

▶️ Start the Bot

`rtmps`

Expected output:

🎵 RTMPS running


---

## 🔑 Per-Chat Setup (Required)

Each Telegram group or channel must configure its own RTMPS stream.

Inside the target chat:

`/setup`

Follow the prompts:

1. Send RTMPS URL


2. Send RTMPS Stream Key



Example:

`/setup`
rtmps://dc5-1.rtmp.t.me/s/
AOV1a58_FgtC2oPzneeehUg

Configuration is stored per chat, allowing unlimited simultaneous streams.


---

🎵 Music Commands

All commands operate independently per chat.

▶️ Play (reply-based)

Reply to an audio file:

`*play`

If music is already playing, the track is added to the queue.


---

⏭️ Skip

`*skip`

Skips the current track and plays the next one (if available).


---

📜 Queue

`*queue`

Shows:

Currently playing track

Up to 10 upcoming tracks

Remaining count (+ n more)



---

🔀 Shuffle Queue

`*shuffle`


---

🔁 Loop Current Track

`*loop current <n>`

Example:

`*loop current 3`


---

🧹 Clear Queue

`*clearqueue`

(Current track continues playing.)


---

## 🧠 Architecture Overview

Telethon for Telegram MTProto communication

- FFmpeg for RTMPS audio streaming

- One player per chat

- One FFmpeg process per chat

- Fully asynchronous, non-blocking design

- Restart-safe configuration storage



---

## 📁 Configuration Files

```~/.rtmps/
├── config.json   # Global Telegram credentials
└── chats.json    # Per-chat RTMPS configuration
```

---

## 🚧 Roadmap

`*stream <profile> support`

Song metadata via info.json

- Admin-only permissions

- Persistent queue resume after restart

- FFmpeg crash auto-recovery

- Optional web dashboard



---

## 🛡️ Requirements

- Python 3.8+

- FFmpeg

- Telegram bot with voice chat permissions

- RTMPS-enabled voice chat



---

## 📜 License

PolyForm Noncommercial License © 2026  
[Ankit Chaubey](https://github.com/ankit-chaubey)

Educational and non-commercial use only.

---

## 🔗 Links

- GitHub: https://github.com/ankit-chaubey/rtmps
- Issues: https://github.com/ankit-chaubey/rtmps/issues

---

## 📬 Contact

For educational, non-commercial use, questions, or feedback:

- GitHub: [@ankit-chaubey](https://github.com/ankit-chaubey)
- Email: [Write Me](mailto:m.ankitchaubey@gmail.com)
- Telegram: [@ankify](https://t.me/ankify)
---

