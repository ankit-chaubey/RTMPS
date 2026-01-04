import os
import asyncio
import random
from telethon import events

from rtmps.player import get_player
from rtmps.ffmpeg import start
from rtmps.storage import load_chats, save_chats

# ================= SETUP STATE =================

SETUP_STATE = {}   # chat_id -> "url" | "key"

# ================= HELPERS =================

def safe_delete(path):
    if path and os.path.exists(path):
        os.remove(path)

def msg_link(chat_id, msg_id):
    cid = str(chat_id)
    if cid.startswith("-100"):
        cid = cid[4:]
    return f"https://t.me/c/{cid}/{msg_id}"

# ================= REGISTER =================

def register(client):

    # ---------- /setup ----------
    @client.on(events.NewMessage(pattern=r'^/setup$'))
    async def setup_start(event):
        SETUP_STATE[event.chat_id] = "url"
        await event.reply("🔧 Send RTMPS URL (plain text)")

    @client.on(events.NewMessage(pattern=r'^/setup\s+'))
    async def setup_invalid(event):
        await event.reply("❌ Use `/setup` only")

    @client.on(events.NewMessage)
    async def setup_flow(event):
        chat_id = event.chat_id
        if chat_id not in SETUP_STATE:
            return

        if event.text.startswith("/"):
            await event.reply("❌ Send plain text, not commands")
            return

        chats = load_chats()
        chats.setdefault(str(chat_id), {})

        if SETUP_STATE[chat_id] == "url":
            chats[str(chat_id)]["rtmps_url"] = event.text.strip()
            SETUP_STATE[chat_id] = "key"
            save_chats(chats)
            await event.reply("✅ URL saved\nNow send RTMPS KEY")

        elif SETUP_STATE[chat_id] == "key":
            chats[str(chat_id)]["rtmps_key"] = event.text.strip()
            save_chats(chats)
            SETUP_STATE.pop(chat_id)
            await event.reply("🎉 Setup complete for this chat")

    # ================= *PLAY =================

    @client.on(events.NewMessage(pattern=r'^\*play$'))
    async def play_handler(event):
        reply = await event.get_reply_message()
        if not reply or not reply.audio:
            return await event.reply("❌ Reply to an audio file with `*play`")

        player = get_player(event.chat_id)
        status = await event.reply("⬇️ **Downloading… hold on 🕊️**")

        if player.process is None:
            file_path = await reply.download_media()
            player.current_msg = reply
            player.current_file = file_path
            player.process = start(event.chat_id, file_path)
            player.loop_count = 0

            await status.edit(
                f"▶ **Now Playing**\n"
                f"🎵 {reply.file.name}\n"
                f"🔗 {msg_link(event.chat_id, reply.id)}"
            )

            await prepare_next(client, event.chat_id)

        else:
            player.queue.append(reply.id)
            await status.edit(
                f"📥 **Added to Queue**\n"
                f"🎵 {reply.file.name}\n"
                f"🔗 {msg_link(event.chat_id, reply.id)}"
            )
            await prepare_next(client, event.chat_id)

    # ================= *QUEUE =================

    @client.on(events.NewMessage(pattern=r'^\*queue$'))
    async def queue_handler(event):
        player = get_player(event.chat_id)
        lines = []

        if player.current_msg:
            lines.append(
                "▶ **Now Playing**\n"
                f"🎵 {player.current_msg.file.name}\n"
                f"🔗 {msg_link(event.chat_id, player.current_msg.id)}\n"
            )

        upcoming = []
        if player.next_msg:
            upcoming.append(player.next_msg.id)
        upcoming.extend(player.queue)

        if upcoming:
            lines.append("⏭ **Up Next**")
            show = upcoming[:10]

            for i, mid in enumerate(show, start=1):
                lines.append(f"{i}. {mid}\n   {msg_link(event.chat_id, mid)}")

            if len(upcoming) > 10:
                lines.append(f"\n➕ **{len(upcoming) - 10} more**")
        else:
            lines.append("⛔ Queue empty")

        await event.reply("\n".join(lines))

    # ================= *SKIP =================

    @client.on(events.NewMessage(pattern=r'^\*skip$'))
    async def skip_handler(event):
        player = get_player(event.chat_id)
        if not player.process:
            return await event.reply("❌ Nothing playing")

        player.process.terminate()
        player.loop_count = 0
        reset_current(player)

        if player.next_file:
            start_next(player)
            await prepare_next(client, event.chat_id)
        else:
            await event.reply("⛔ Queue empty")

    # ================= *SHUFFLE =================

    @client.on(events.NewMessage(pattern=r'^\*shuffle$'))
    async def shuffle_handler(event):
        player = get_player(event.chat_id)
        if not player.queue:
            return await event.reply("⛔ Queue empty")

        random.shuffle(player.queue)
        await event.reply("🔀 **Queue shuffled**")

    # ================= *CLEARQUEUE =================

    @client.on(events.NewMessage(pattern=r'^\*clearqueue$'))
    async def clearqueue_handler(event):
        player = get_player(event.chat_id)
        player.queue.clear()
        await event.reply("🧹 **Queue cleared (current keeps playing)**")

    # ================= *LOOP =================

    @client.on(events.NewMessage(pattern=r'^\*loop current (\d+)$'))
    async def loop_handler(event):
        player = get_player(event.chat_id)
        if not player.current_msg:
            return await event.reply("❌ Nothing is playing")

        n = int(event.pattern_match.group(1))
        player.loop_count = n
        await event.reply(f"🔁 **Current song will loop {n} times**")


# ================= PLAYER HELPERS =================

async def prepare_next(client, chat_id):
    player = get_player(chat_id)
    if player.next_file is None and player.queue:
        mid = player.queue.pop(0)
        msg = await client.get_messages(chat_id, ids=mid)
        path = await msg.download_media()
        player.next_msg = msg
        player.next_file = path

def reset_current(player):
    safe_delete(player.current_file)
    player.process = None
    player.current_msg = None
    player.current_file = None

def start_next(player):
    player.current_msg = player.next_msg
    player.current_file = player.next_file
    player.process = start(player.chat_id, player.current_file)
    player.next_msg = None
    player.next_file = None
