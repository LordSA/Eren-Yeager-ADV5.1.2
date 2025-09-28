import os
import traceback
from io import BytesIO
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
import re
from Script import script
from lang import tts

def detect_language(text: str) -> str:
    """Auto-detect language from text using Unicode ranges."""
    for lang, pattern in tts.LANGUAGE_PATTERNS.items():
        if pattern.search(text):
            return lang
    return "english"  # Default to English

def get_voice(voice: str) -> str:
    """Get valid voice name, support both English voices and Indian languages."""
    if not voice:
        return "coral"
    
    v = voice.lower().strip()
    
    # Check if it's an Indian language
    if v in tts.INDIAN_LANGUAGES:
        return tts.INDIAN_LANGUAGES[v]
    
    # Check if it's an English voice
    if v in tts.VOICES:
        return v
    
    # Default fallback
    return "coral"

async def fetch_tts_audio(text: str, voice: str = "coral", speed: str = "1.00") -> BytesIO:
    """
    Fetch TTS audio from ttsmp3.com API with Indian language support.
    """
    voice = get_voice(voice)
    
    # Ensure text is properly encoded and cleaned
    text = str(text).strip()
    if not text:
        raise Exception("Empty text provided")
    
    # Limit text length to avoid API issues
    if len(text) > 3000:
        text = text[:3000] + "..."
    
    payload = {
        "msg": text,
        "lang": voice,
        "speed": speed,
        "source": "ttsmp3"
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers=headers
        ) as session:
            # Make POST request to TTS API
            async with session.post(
                "https://ttsmp3.com/makemp3_ai.php", 
                data=payload,
                timeout=15
            ) as resp:
                if resp.status != 200:
                    raise Exception(f"HTTP {resp.status}: Server error")
                
                try:
                    data = await resp.json()
                except Exception as e:
                    raise Exception(f"Failed to parse API response: {e}")
                
                # Check for API errors
                if data.get("Error") == "Usage Limit exceeded":
                    raise Exception("TTS API usage limit exceeded. Please try again later.")
                
                if data.get("Error") != 0 or not data.get("URL"):
                    error_msg = data.get("Error", "Unknown error")
                    raise Exception(f"TTS generation failed: {error_msg}")
                
                audio_url = data["URL"]
                
                # Download audio file
                async with session.get(audio_url, timeout=20) as audio_resp:
                    if audio_resp.status != 200:
                        raise Exception(f"Failed to download audio: HTTP {audio_resp.status}")
                    
                    audio_bytes = await audio_resp.read()
                    if len(audio_bytes) == 0:
                        raise Exception("Received empty audio file")
                    
                    audio = BytesIO(audio_bytes)
                    audio.name = f"tts_{voice}.mp3"
                    audio.seek(0)
                    return audio
                    
    except aiohttp.ClientError as e:
        raise Exception(f"Network error: {e}")
    except Exception as e:
        raise Exception(f"TTS error: {e}")

@Client.on_message(filters.command("tts"))
async def text_to_speech(client: Client, message: Message):
    """
    Telegram bot handler for /tts command with Indian language support.
    """
    try:
        # Check if replying to a message with text
        if not message.reply_to_message:
            return await message.reply_text(
                "❌ Please reply to a message containing text.\n"
                "Usage: Reply to a text message and use /tts\n"
                "Example: /tts malayalam, /tts hindi, /tts tamil"
            )
        
        # Get text from replied message
        text_to_convert = None
        if message.reply_to_message.text:
            text_to_convert = message.reply_to_message.text
        elif message.reply_to_message.caption:
            text_to_convert = message.reply_to_message.caption
        
        if not text_to_convert or not text_to_convert.strip():
            return await message.reply_text("❌ The replied message doesn't contain any text.")
        
        # Parse voice/language from command
        voice = "coral"  # default voice
        command_args = message.text.split()[1:] if len(message.text.split()) > 1 else []
        
        if command_args:
            voice = get_voice(command_args[0])
        else:
            # Auto-detect language if no argument provided
            detected_lang = detect_language(text_to_convert)
            if detected_lang != "english":
                voice = get_voice(detected_lang)
                print(f"Auto-detected language: {detected_lang}")
        
        # Show processing message
        lang_display = voice if voice in tts.INDIAN_LANGUAGES.values() else f"voice: {voice}"
        m = await message.reply_text(
            f"🎙️ Converting text to speech using {lang_display}\n"
            f"Text length: {len(text_to_convert)} characters"
        )
        
        # Generate TTS audio
        audio_file = await fetch_tts_audio(text_to_convert, voice)
        
        # Send audio file
        await message.reply_audio(
            audio_file,
            caption=f"🎵 TTS Audio ({lang_display})",
            performer="TTS Bot",
            title=f"TTS - {lang_display}"
        )
        
        # Delete processing message
        await m.delete()
        
    except Exception as e:
        error_msg = str(e)
        try:
            await m.edit_text(f"❌ Error: {error_msg}")
        except:
            await message.reply_text(f"❌ Error: {error_msg}")
        
        # Log full error for debugging
        print(f"TTS Error: {error_msg}")
        print(traceback.format_exc())

@Client.on_message(filters.command("ttshelp"))
async def tts_help(client: Client, message: Message):
    """Show TTS help information with Indian language support."""
    help_text = script.TTS_HELP
    await message.reply_text(help_text)

