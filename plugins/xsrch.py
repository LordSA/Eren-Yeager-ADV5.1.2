# xnxx_plugin.py
import aiohttp
from pyrogram import Client, filters

# Temporary storage for search results
temp_results = []

USE_AD_THUMB = True

async def get_thumb(url: str):
    """Download image from URL as bytes."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.read()
    except:
        return None

# ------------------- XSEARCH -------------------
@Client.on_message(filters.command("xsearch") & filters.private)
async def xsearch(client, message):
    query = " ".join(message.command[1:]).strip()
    if not query:
        return await message.reply("❌ Provide a search query!\nExample:\nxsearch Big Boobs")

    await message.reply("🔎 Searching videos...")
    try:
        api = f"https://api-aswin-sparky.koyeb.app/api/search/xnxx?search={query}"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as resp:
                data = await resp.json()

        if not data.get("status") or not data.get("result", {}).get("status"):
            msg = "❌ Failed to fetch search results."
            if data.get("message"):
                msg += f"\n_API message: {data['message']}_"
            return await message.reply(msg)

        results = data["result"]["result"]
        if not results:
            return await message.reply("No videos found for your query!")

        global temp_results
        temp_results = results[:10]  # store top 10 results
        reply = f"*Search Results for:* {query}\n\n"
        for i, v in enumerate(temp_results, 1):
            reply += f"*{i}. {v['title']}*\n{v['info'].replace(chr(10), ' ').strip()}\n[Link]({v['link']})\n\n"
        reply += "Reply with the number to download, e.g. xvideo <number>"
        await message.reply(reply)

    except Exception as e:
        print("XNXX Search Plugin Error:", e)
        await message.reply("⚠ Failed to search. Try again later!")

# ------------------- XVIDEO -------------------
@Client.on_message(filters.command("xvideo") & filters.private)
async def xvideo(client, message):
    arg = " ".join(message.command[1:]).strip()
    if not arg:
        return await message.reply("❌ Provide video number or URL!\nExample:\nxvideo 1 or xvideo <url>")

    # If number, fetch from previous search
    try:
        idx = int(arg) - 1
        video_url = temp_results[idx]["link"]
    except:
        video_url = arg

    await message.reply("⏳ Fetching video details...")

    try:
        api = f"https://api-aswin-sparky.koyeb.app/api/downloader/xnxx?url={video_url}"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as resp:
                data = await resp.json()

        if not data.get("status") or not data.get("data", {}).get("files"):
            msg = "❌ Failed to fetch video. Try another link!"
            if data.get("message"):
                msg += f"\n_API message: {data['message']}_"
            return await message.reply(msg)

        video_data = data["data"]
        video_file = video_data["files"].get("high") or video_data["files"].get("low")
        if not video_file:
            return await message.reply("❌ No downloadable video found!")

        title = video_data.get("title", "xnxx_video")[:32].replace(" ", "_")
        duration = video_data.get("duration", "Unknown")
        caption = f"*{title}*\n\n_Duration:_ {duration} sec"

        custom_thumb = await get_thumb("https://i.ibb.co/G4Yk3Qfy/temp.jpg") if USE_AD_THUMB else None
        video_thumb = await get_thumb(video_data.get("image"))

        await client.send_document(
            message.chat.id,
            video_file,
            file_name=f"{title}.mp4",
            caption=caption,
            thumb=video_thumb or custom_thumb
        )

    except Exception as e:
        print("XNXX Plugin Error:", e)
        await message.reply("⚠ Failed to download or send the video. Try again later!")
