import os
import traceback
from gtts import gTTS
from io import BytesIO
from langdetect import detect
from asyncio import get_running_loop
from pyrogram import Client, filters
from pyrogram.types import Message

# Import your dictionary
from plugins.Tools.list import list


def convert(text: str):
    """Convert text to speech using gTTS with langdetect + custom list mapping"""
    try:
        # Detect language
        detected_lang = detect(text)  # e.g., "ml", "hi", "en"
        lang_code = None

        # Map with your list.py (values are already codes like "ml")
        for name, code in list.items():
            if code == detected_lang or name.lower() == detected_lang.lower():
                lang_code = code
                break

        if not lang_code:  # fallback
            lang_code = "en"

        # Generate TTS
        file_path = "tts_output.mp3"
        tts = gTTS(text=text, lang=lang_code)
        tts.save(file_path)

        return file_path
    except Exception as e:
        raise RuntimeError(f"TTS conversion failed: {e}")


@Client.on_message(filters.command("tts"))
async def text_to_speech(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply_text("⚠️ Reply to a text message with /tts")

    m = await message.reply_text("⏳ Processing...")

    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        file_path = await loop.run_in_executor(None, convert, text)

        await message.reply_voice(file_path)  # Voice message in Telegram
        await m.delete()

        if os.path.exists(file_path):
            os.remove(file_path)

    except Exception as e:
        await m.edit(f"❌ Error: {e}")
        print(traceback.format_exc())
