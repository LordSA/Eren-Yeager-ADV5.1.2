from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.connections_mdb import add_connection, all_connections, if_active, delete_connection
from info import ADMINS
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@Client.on_message((filters.private | filters.group) & filters.command('connect'))
async def addconnection(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are anonymous admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>𝙴𝚗𝚝𝚎𝚛 𝚒𝚗 𝚌𝚘𝚛𝚛𝚎𝚌𝚝 𝚏𝚘𝚛𝚖𝚊𝚝!</b>\n\n"
                "<code>/𝚌𝚘𝚗𝚗𝚎𝚌𝚝 𝚐𝚛𝚘𝚞𝚙𝚒𝚍</code>\n\n"
                "<i>𝙶𝚎𝚝 𝚢𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙 𝚒𝚍 𝚋𝚢 𝚊𝚍𝚍𝚒𝚗𝚐 𝚝𝚑𝚒𝚜 𝚋𝚘𝚝 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙 𝚊𝚗𝚍 𝚞𝚜𝚎  <code>/id</code></i>",
                quote=True
            )
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (
                st.status != enums.ChatMemberStatus.ADMINISTRATOR
                and st.status != enums.ChatMemberStatus.OWNER
                and userid not in ADMINS
        ):
            await message.reply_text("You should be an admin in Given group!", quote=True)
            return
    except Exception as e:
        logger.exception(e)
        await message.reply_text(
            "Invalid Group ID!\n\nIf correct, Make sure I'm present in your group!!",
            quote=True,
        )

        return
    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == enums.ChatMemberStatus.ADMINISTRATOR:
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Successfully connected to **{title}**\nNow manage your group from my pm !",
                    quote=True,
                    parse_mode=enums.ParseMode.MARKDOWN
                )
                if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                    await client.send_message(
                        userid,
                        f"Connected to **{title}** !",
                        parse_mode=enums.ParseMode.MARKDOWN
                    )
            else:
                await message.reply_text(
                    "𝚈𝚘𝚞'𝚛𝚎 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚝𝚘 𝚝𝚑𝚒𝚜 𝚌𝚑𝚊𝚝!",
                    quote=True
                )
        else:
            await message.reply_text("𝙰𝚍𝚍 𝚖𝚎 𝚊𝚜 𝚊𝚗 𝚊𝚍𝚖𝚒𝚗 𝚒𝚗 𝚐𝚛𝚘𝚞𝚙", quote=True)
    except Exception as e:
        logger.exception(e)
        await message.reply_text('𝚂𝚘𝚖𝚎 𝚎𝚛𝚛𝚘𝚛 𝚘𝚌𝚌𝚞𝚛𝚛𝚎𝚍! 𝚃𝚛𝚢 𝚊𝚐𝚊𝚒𝚗 𝚕𝚊𝚝𝚎𝚛.', quote=True)
        return


@Client.on_message((filters.private | filters.group) & filters.command('disconnect'))
async def deleteconnection(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"𝚈𝚘𝚞 𝚊𝚛𝚎 𝚊𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜 𝚊𝚍𝚖𝚒𝚗. 𝚄𝚜𝚎 /𝚌𝚘𝚗𝚗𝚎𝚌𝚝 {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        await message.reply_text("𝚁𝚞𝚗 /𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗𝚜 𝚝𝚘 𝚟𝚒𝚎𝚠 𝚘𝚛 𝚍𝚒𝚜𝚌𝚘𝚗𝚗𝚎𝚌𝚝 𝚏𝚛𝚘𝚖 𝚐𝚛𝚘𝚞𝚙𝚜!", quote=True)

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if (
                st.status != enums.ChatMemberStatus.ADMINISTRATOR
                and st.status != enums.ChatMemberStatus.OWNER
                and str(userid) not in ADMINS
        ):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚍𝚒𝚜𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚏𝚛𝚘𝚖 𝚝𝚑𝚒𝚜 𝚌𝚑𝚊𝚝", quote=True)
        else:
            await message.reply_text("𝚃𝚑𝚒𝚜 𝚌𝚑𝚊𝚝 𝚒𝚜𝚗'𝚝 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚝𝚘 𝚖𝚎!\n𝙳𝚘 /𝚌𝚘𝚗𝚗𝚎𝚌𝚝 𝚝𝚘 𝚌𝚘𝚗𝚗𝚎𝚌𝚝.", quote=True)


@Client.on_message(filters.private & filters.command(["connections"]))
async def connections(client, message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "𝚃𝚑𝚎𝚛𝚎 𝚊𝚛𝚎 𝚗𝚘 𝚊𝚌𝚝𝚒𝚟𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗𝚜!! 𝙲𝚘𝚗𝚗𝚎𝚌𝚝 𝚝𝚘 𝚜𝚘𝚖𝚎 𝚐𝚛𝚘𝚞𝚙𝚜 𝚏𝚒𝚛𝚜𝚝.",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            act = " - ACTIVE" if active else ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "𝚈𝚘𝚞𝚛 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍 𝚐𝚛𝚘𝚞𝚙 𝚍𝚎𝚝𝚊𝚒𝚕𝚜 ;\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    else:
        await message.reply_text(
            "𝚃𝚑𝚎𝚛𝚎 𝚊𝚛𝚎 𝚗𝚘 𝚊𝚌𝚝𝚒𝚟𝚎 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗𝚜!! 𝙲𝚘𝚗𝚗𝚎𝚌𝚝 𝚝𝚘 𝚜𝚘𝚖𝚎 𝚐𝚛𝚘𝚞𝚙𝚜 𝚏𝚒𝚛𝚜𝚝.",
            quote=True
        )
