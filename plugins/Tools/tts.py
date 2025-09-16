import os
import traceback
from io import BytesIO
from gtts import gTTS
from googletrans import Translator
from asyncio import get_running_loop
from pyrogram import Client, filters
from pyrogram.types import Message


def convert(text: str):
    """Convert text to speech using gTTS with auto language detection"""
    try:
        # Detect language
        detected = Translator().translate(text, dest="en")
        lang = detected.src

        # Generate TTS
        file_path = "tts_output.mp3"
        tts = gTTS(text=text, lang=lang)
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

        # Reply as voice (so it plays inline in Telegram)
        await message.reply_voice(file_path)

        await m.delete()

        if os.path.exists(file_path):
            os.remove(file_path)

    except Exception as e:
        await m.edit(f"❌ Error: {e}")
        print(traceback.format_exc())
