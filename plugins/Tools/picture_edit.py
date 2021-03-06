from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from info import VIDS
import random

@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            #video=random.choice(VIDS),
            text="Select your required mode from below!γ€γ€",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('γπ±ππΈπΆπ·πγ', callback_data="bright"),
                        InlineKeyboardButton('γπΌπΈππ΄π³γ', callback_data="mix"),
                        InlineKeyboardButton('γπ± & πγ', callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton('γπ²πΈππ²π»π΄γ', callback_data="circle"),
                        InlineKeyboardButton('γπ±π»ππγ', callback_data="blur"),
                        InlineKeyboardButton('γπ±πΎππ³π΄πγ', callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton('γπππΈπ²πΊπ΄πγ', callback_data="stick"),
                        InlineKeyboardButton('γππΎππ°ππ΄γ', callback_data="rotate"),
                        InlineKeyboardButton('γπ²πΎπ½πππ°ππγ', callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton('γππ΄πΏπΈπ°γ', callback_data="sepia"),
                        InlineKeyboardButton('γπΏπ΄π½π²πΈπ»γ', callback_data="pencil"),
                        InlineKeyboardButton('γπ²π°πππΎπΎπ½γ', callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton('γπΈπ½ππ΄ππγ', callback_data="inverted"),
                        InlineKeyboardButton('γπΆπ»πΈππ²π·γ', callback_data="glitch"),
                        InlineKeyboardButton('γππ΄πΌπΎππ΄ π±πΆγ', callback_data="removebg"),
                    ],
                    [
                        InlineKeyboardButton('γπ±π°π²πΊγ', callback_data="help"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
