import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InputMediaVideo, InputMediaDocument
from utils import temp  # If you use temp dict for states

USE_AD_THUMB = True  # You can control this from env or config

# --------------------- XNXX SEARCH ---------------------
@Client.on_message(filters.command("xsearch") & filters.private)
async def xsearch(client, message):
    query = " ".join(message.command[1:]).strip()
    if not query:
        return await message.reply(
            "❌ Provide a search query!\nExample:\n/xsearch Big Boobs"
        )

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

        reply = f"*Search Results for:* {query}\n\n"
        for i, v in enumerate(results[:10], 1):
            reply += f"*{i}. {v['title']}*\n{v['info'].replace(chr(10), ' ').strip()}\n[Link]({v['link']})\n\n"

        reply += "Reply with the number to download, e.g. /xvideo <link>"
        await message.reply(reply)

    except Exception as e:
        print("XNXX Search Plugin Error:", e)
        await message.reply("⚠ Failed to search. Try again later!")


# --------------------- XNXX VIDEO DOWNLOAD ---------------------
@Client.on_message(filters.command("xvideo") & filters.private)
async def xvideo(client, message):
    url = " ".join(message.command[1:]).strip()
    if not url:
        return await message.reply(
            "❌ Provide a valid xnxx/xvideos URL!\nExample:\n/xvideo https://www.xvideos.com/videoXXXXX/title"
        )

    await message.reply("⏳ Fetching video details...")

    try:
        api = f"https://api-aswin-sparky.koyeb.app/api/downloader/xnxx?url={url}"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as resp:
                data = await resp.json()

        if not data.get("status") or not data.get("data", {}).get("files"):
            msg = "❌ Failed to fetch video. Try another link!"
            if data.get("message"):
                msg += f"\n_API message: {data['message']}_"
            return await message.reply(msg)

        video_data = data["data"]
        video_url = video_data["files"].get("high") or video_data["files"].get("low")
        if not video_url:
            return await message.reply("❌ No downloadable video found!")

        title = video_data.get("title", "xnxx_video")
        duration = video_data.get("duration", "Unknown")
        caption = f"*{title}*\n\n_Duration:_ {duration} sec"

        # Download thumbnail if needed
        async def get_thumb(url):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as r:
                        return await r.read()
            except:
                return None

        custom_thumb = await get_thumb("https://i.ibb.co/G4Yk3Qfy/temp.jpg") if USE_AD_THUMB else None
        video_thumb = await get_thumb(video_data.get("image"))

        # Check file size
        file_size = 0
        try:
            async with aiohttp.ClientSession() as session:
                async with session.head(video_url) as r:
                    file_size = int(r.headers.get("content-length", 0))
        except:
            pass

        max_size = 64 * 1024 * 1024
        if file_size and file_size > max_size:
            return await message.reply(f"⚠ File too large for Telegram.\nDownload manually:\n{video_url}")

        await client.send_document(
            message.chat.id,
            video_url,
            file_name=f"{title[:32].replace(' ', '_')}.mp4",
            caption=caption,
            thumb=video_thumb or custom_thumb,
        )

    except Exception as e:
        print("XNXX Plugin Error:", e)
        await message.reply("⚠ Failed to download or send the video. Try again later!")
