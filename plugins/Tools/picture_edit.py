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
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('『𝙱𝚁𝙸𝙶𝙷𝚃』', callback_data="bright"),
                        InlineKeyboardButton('『𝙼𝙸𝚇𝙴𝙳』', callback_data="mix"),
                        InlineKeyboardButton('『𝙱 & 𝚆』', callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton('『𝙲𝙸𝚁𝙲𝙻𝙴』', callback_data="circle"),
                        InlineKeyboardButton('『𝙱𝙻𝚄𝚁』', callback_data="blur"),
                        InlineKeyboardButton('『𝙱𝙾𝚁𝙳𝙴𝚁』', callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton('『𝚂𝚃𝙸𝙲𝙺𝙴𝚁』', callback_data="stick"),
                        InlineKeyboardButton('『𝚁𝙾𝚃𝙰𝚃𝙴』', callback_data="rotate"),
                        InlineKeyboardButton('『𝙲𝙾𝙽𝚃𝚁𝙰𝚂𝚃』', callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton('『𝚂𝙴𝙿𝙸𝙰』', callback_data="sepia"),
                        InlineKeyboardButton('『𝙿𝙴𝙽𝙲𝙸𝙻』', callback_data="pencil"),
                        InlineKeyboardButton('『𝙲𝙰𝚁𝚃𝙾𝙾𝙽』', callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton('『𝙸𝙽𝚅𝙴𝚁𝚃』', callback_data="inverted"),
                        InlineKeyboardButton('『𝙶𝙻𝙸𝚃𝙲𝙷』', callback_data="glitch"),
                        InlineKeyboardButton('『𝚁𝙴𝙼𝙾𝚅𝙴 𝙱𝙶』', callback_data="removebg"),
                    ],
                    [
                        InlineKeyboardButton('『𝙱𝙰𝙲𝙺』', callback_data="help"),
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
