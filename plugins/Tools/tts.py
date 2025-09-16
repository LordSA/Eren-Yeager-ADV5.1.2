import os
import traceback
from io import BytesIO
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message

VOICES = [
    "nova", "alloy", "ash", "coral", "echo",
    "fable", "onyx", "sage", "shimmer"
]

def get_voice(voice: str) -> str:
    if not voice:
        return "coral"
    v = voice.lower()
    return v if v in VOICES else "coral"

async def fetch_tts_audio(text: str, voice: str = "coral", speed: str = "1.00") -> BytesIO:
    """
    Fetch TTS audio from ttsmp3.com API and return as BytesIO.
    """
    voice = get_voice(voice)
    payload = {
        "msg": text,
        "lang": voice,
        "speed": speed,
        "source": "ttsmp3"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://ttsmp3.com/makemp3_ai.php", data=payload) as resp:
            data = await resp.json()
            if data.get("Error") == "Usage Limit exceeded":
                raise Exception("TTS API usage limit exceeded")
            if data.get("Error") != 0 or not data.get("URL"):
                raise Exception(f"TTS generation failed: {data}")

            audio_url = data["URL"]
            async with session.get(audio_url) as audio_resp:
                audio_bytes = await audio_resp.read()
                audio = BytesIO(audio_bytes)
                audio.name = f"{voice}.mp3"
                audio.seek(0)
                return audio

@Client.on_message(filters.command("tts"))
async def text_to_speech(client: Client, message: Message):
    """
    Telegram bot handler for /tts command.
    Replies with TTS audio of the replied message text.
    """
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply_text("Please reply to a message containing text.")

    text_to_convert = message.reply_to_message.text
    voice = "coral"  # default voice, could parse from command args

    m = await message.reply_text("Converting text to speech...")

    try:
        audio_file = await fetch_tts_audio(text_to_convert, voice)
        await message.reply_audio(audio_file)
        await m.delete()
    except Exception as e:
        await m.edit_text(f"❌ An error occurred: {e}")
        print(traceback.format_exc())
