from pyrogram import Client, filters
from utils import temp
from pyrogram.types import Message
from database.users_chats_db import db
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import SUPPORT_CHAT

async def banned_users(_, client, message: Message):
    return (
        message.from_user is not None or not message.sender_chat
    ) and message.from_user.id in temp.BANNED_USERS

banned_user = filters.create(banned_users)

async def disabled_chat(_, client, message: Message):
    return message.chat.id in temp.BANNED_CHATS

disabled_group=filters.create(disabled_chat)


@Client.on_message(filters.private & banned_user & filters.incoming)
async def ban_reply(bot, message):
    ban = await db.get_ban_status(message.from_user.id)
    await message.reply(f'𝚂𝚘𝚛𝚛𝚢 𝙳𝚞𝚍𝚎, 𝚈𝚘𝚞 𝚊𝚛𝚎 𝙱𝚊𝚗𝚗𝚎𝚍 𝚝𝚘 𝚞𝚜𝚎 𝙼𝚎. \𝚗𝙱𝚊𝚗 𝚁𝚎𝚊𝚜𝚘𝚗: {ban["ban_reason"]}')

@Client.on_message(filters.group & disabled_group & filters.incoming)
async def grp_bd(bot, message):
    buttons = [[
        InlineKeyboardButton('𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{SUPPORT_CHAT}')
    ]]
    reply_markup=InlineKeyboardMarkup(buttons)
    vazha = await db.get_chat(message.chat.id)
    k = await message.reply(
        text=f"𝙲𝙷𝙰𝚃 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝙴𝙳 🐞\𝚗\𝚗𝙼𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚑𝚊𝚜 𝚛𝚎𝚜𝚝𝚛𝚒𝚌𝚝𝚎𝚍 𝚖𝚎 𝚏𝚛𝚘𝚖 𝚠𝚘𝚛𝚔𝚒𝚗𝚐 𝚑𝚎𝚛𝚎 ! 𝙸𝚏 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚖𝚘𝚛𝚎 𝚊𝚋𝚘𝚞𝚝 𝚒𝚝 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚜𝚞𝚙𝚙𝚘𝚛𝚝..\𝚗𝚁𝚎𝚊𝚜𝚘𝚗 : <code>{vazha['reason']}</code>.",
        reply_markup=reply_markup)
    try:
        await k.pin()
    except:
        pass
    await bot.leave_chat(message.chat.id)
