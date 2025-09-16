import os
import traceback
from gtts import gTTS
from googletrans import Translator
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import get_running_loop


def convert_text_to_speech(text):
    """
    Converts text to an in-memory audio file (BytesIO) using gTTS.
    The language is automatically detected.
    """
    translator = Translator()
    try:
        translated_text = translator.translate(text)
        detected_lang = translated_text.src
    except Exception as e:
        # Fallback to English if language detection fails
        print(f"Language detection failed: {e}. Defaulting to 'en'.")
        detected_lang = 'en'

    audio = BytesIO()
    tts = gTTS(text=text, lang=detected_lang)
    tts.write_to_fp(audio)
    audio.seek(0)
    audio.name = f"{detected_lang}.mp3"
    return audio

@Client.on_message(filters.command("tts"))
async def text_to_speech(_, message: Message):
    """
    Telegram bot handler for the /tts command.
    Responds to a message with a text-to-speech audio file.
    """
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply_text("Please reply to a message containing text.")

    m = await message.reply_text("Converting text to speech...")
    text_to_convert = message.reply_to_message.text

    try:
        loop = get_running_loop()
        audio_file = await loop.run_in_executor(None, convert_text_to_speech, text_to_convert)
        
        await message.reply_audio(audio_file)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        await m.edit_text(error_message)
        print(traceback.format_exc())
    finally:
        await m.delete()