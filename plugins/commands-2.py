# Made by Lord SA
import os
import logging
import random
import asyncio
import aiohttp
import traceback
from asyncio import get_running_loop
from io import BytesIO
from Script import script
from time import time, sleep
from datetime import datetime
from pyrogram.errors import UserNotParticipant
from plugins.Tools.help_func.extract_user import extract_user
from plugins.Tools.help_func.last_online import last_online
from pyrogram import Client, filters
from urllib.parse import quote
from info import SUPPORT_CHAT
from gtts import gTTS
from telegraph import upload_file
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, VIDS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp
from database.connections_mdb import active_connection
from googletrans import Translator
from plugins.Tools.list import list
from database.gtrans_mdb import find_one
from plugins.Tools.help_func.admin_check import admin_check
from plugins.Tools.help_func.cust_p_filters import f_onw_fliter
from plugins.Tools.help_func.cust_p_filters import admin_fliter
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid
import re
import json
import base64
import requests
logger = logging.getLogger(__name__)

@Client.on_message(filters.command(["torrent", "tor"]))
async def torrent(_, message):
    global m
    global i
    global a
    global query
    try:
        await message.delete()
    except:
        pass
    if len(message.command) < 2:
        await message.reply_text("`/torrent <Movie Name>`")
        return
    query = message.text.split(None, 1)[1].replace(" ", "%20")
    m = await message.reply_text("Searching\nThis might take a while")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://itor.api-zero.workers.dev/?name={query}") \
                    as resp:
                a = json.loads(await resp.text())
    except:
        await m.edit("Found Nothing.")
        return
    result = (
        f"**Page - {i+1}**\n\n"
        f"**🎬 Name :** {a[i]['name']}\n"
        f"**🧲 Link :** `{a[i]['link']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"{emoji.CROSS_MARK} Close",
                                         callback_data="close_data"),
                    InlineKeyboardButton(f"『𝙽𝙴𝚇𝚃』",
                                         callback_data="next_tor")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("next_tor"))
async def callback_query_next(_, message):
    global i
    global m
    global a
    global query
    i += 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"**🎬 Name :** {a[i]['name']}\n"
        f"**🧲 Link :** `{a[i]['link']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"『𝙿𝚁𝙴𝚅』",
                                         callback_data="back_tor"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="close_data"),
                    InlineKeyboardButton(f"『𝙽𝙴𝚇𝚃』",
                                         callback_data="next_tor")
                    
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("back_tor"))
async def callback_query_previous(_, message):
    global i
    global m
    global a
    global query
    i -= 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"**🎬 Name:** {a[i]['name']}\n"
        f"**🧲 Link:** `{a[i]['link']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"『𝙿𝚁𝙴𝚅』",
                                         callback_data="back_tor"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="close_data"),
                    InlineKeyboardButton(f"『𝙽𝙴𝚇𝚃』",
                                         callback_data="next_tor")
                ]
            ]
        ),
        parse_mode="markdown",
    )

@Client.on_message(filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			hehek = InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            text=f"『𝙼𝙾𝚁𝙴 𝙻𝙰𝙽𝙶 𝙲𝙾𝙳𝙴𝚂』", url="https://cloud.google.com/translate/docs/languages"
                                        )
                                    ],
				    [
                                        InlineKeyboardButton(
                                            "『𝙲𝙻𝙾𝚂𝙴』", callback_data="close_data"
                                        )
                                    ],
                                ]
                            )
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"translated from {fromt.capitalize()} to {to.capitalize()}\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			except:
			   	await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			

		except :
			print("error")
	else:
			 ms = await message.reply_text("You can Use This Command by using reply to message")
			 await ms.delete()

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")

@Client.on_message(filters.command(["json", 'js', 'showjson']))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
    try:
        pk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🚫 Cʟᴏsᴇ",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_text(f"<code>{the_real_message}</code>", reply_markup=pk, quote=True)
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🚫 Cʟᴏsᴇ",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            quote=True,
            reply_markup=reply_markup
        )            
        os.remove("json.text")

TG_MAX_SELECT_LEN = 400

@Client.on_message(
    filters.command("purge") &
    f_onw_fliter
)
async def purge(client, message):
    """ purge upto the replied message """
    if message.chat.type not in (("supergroup", "channel")):
        # https://t.me/c/1312712379/84174
        return

    is_admin = await admin_check(message)

    if not is_admin:
        return

    status_message = await message.reply_text("...", quote=True)
    await message.delete()
    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(
            message.reply_to_message.message_id,
            message.message_id
        ):
            message_ids.append(a_s_message_id)
            if len(message_ids) == TG_MAX_SELECT_LEN:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=message_ids,
                    revoke=True
                )
                count_del_etion_s += len(message_ids)
                message_ids = []
        if len(message_ids) > 0:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message_ids,
                revoke=True
            )
            count_del_etion_s += len(message_ids)

    await status_message.edit_text(
        f"deleted {count_del_etion_s} messages"
    )
    await asyncio.sleep(5)
    await status_message.delete()

@Client.on_message(
    filters.command(["pin"]) &
    admin_fliter
)
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()

@Client.on_message(
    filters.command(["unpin"]) &
    admin_fliter
)
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()

@Client.on_message(filters.incoming & ~filters.private & filters.command('inkick'))
def inkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == ("creator"):
    if len(message.command) > 1:
      input_str = message.command
      sent_message = message.reply_text(script.START_KICK)
      sleep(20)
      sent_message.delete()
      message.delete()
      count = 0
      for member in client.iter_chat_members(message.chat.id):
        if member.user.status in input_str and not member.status in ('administrator', 'creator'):
          try:
            client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
            count += 1
            sleep(1)
          except (ChatAdminRequired, UserAdminInvalid):
            sent_message.edit(script.ADMIN_REQUIRED)
            client.leave_chat(message.chat.id)
            break
          except FloodWait as e:
            sleep(e.x)
      try:
        sent_message.edit(script.KICKED.format(count))
      except ChatWriteForbidden:
        pass
    else:
      message.reply_text(script.INPUT_REQUIRED)
  else:
    sent_message = message.reply_text(script.CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()
    message.delete()

@Client.on_message(filters.incoming & ~filters.private & filters.command('dkick'))
def dkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == ("creator"):
    sent_message = message.reply_text(script.START_KICK)
    sleep(20)
    sent_message.delete()
    message.delete()
    count = 0
    for member in client.iter_chat_members(message.chat.id):
      if member.user.is_deleted and not member.status in ('administrator', 'creator'):
        try:
          client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
          count += 1
          sleep(1)
        except (ChatAdminRequired, UserAdminInvalid):
          sent_message.edit(script.ADMIN_REQUIRED)
          client.leave_chat(message.chat.id)
          break
        except FloodWait as e:
          sleep(e.x)
    try:
      sent_message.edit(script.DKICK.format(count))
    except ChatWriteForbidden:
      pass
  else:
    sent_message = message.reply_text(script.CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()
    message.delete()

@Client.on_message(filters.incoming & ~filters.private & filters.command('instatus'))
def instatus(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status in ('administrator', 'creator', 'ADMINS'):
    sent_message = message.reply_text(script.FETCHING_INFO)
    recently = 0
    within_week = 0
    within_month = 0
    long_time_ago = 0
    deleted_acc = 0
    uncached = 0
    bot = 0
    for member in client.iter_chat_members(message.chat.id):
      user = member.user
      if user.is_deleted:
        deleted_acc += 1
      elif user.is_bot:
        bot += 1
      elif user.status == "recently":
        recently += 1
      elif user.status == "within_week":
        within_week += 1
      elif user.status == "within_month":
        within_month += 1
      elif user.status == "long_time_ago":
        long_time_ago += 1
      else:
        uncached += 1
    sent_message.edit(script.STATUS.format(message.chat.title, recently, within_week, within_month, long_time_ago, deleted_acc, bot, uncached))

#paste py
#Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

#Pastebins
async def p_paste(message, extension=None):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        return {
            "url": purl,
            "raw": f"https://pasty.lus.pm/{response['id']}/raw",
            "bin": "Pasty",
        }
    return {"error": "Unable to reach pasty.lus.pm"}




    
    
@Client.on_message(filters.command(["tgpaste", "pasty", "paste"]))
async def pasty(client, message):
    pablo = await message.reply_text("`Please wait...`")
    tex_t = message.text
    message_s = tex_t
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("`Only text and documents are supported.`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text
    
    ext = "py"
    x = await p_paste(message_s, ext)
    p_link = x["url"]
    p_raw = x["raw"]
    
    pasted = f"**Successfully Paste to Pasty**\n\n**Link:** • [Click here]({p_link})\n\n**Raw Link:** • [Click here]({p_raw})"
    await pablo.edit(pasted, disable_web_page_preview=True)

#Generate Password
@Client.on_message(filters.command(["genpassword", 'genpw']))
async def password(bot, update):
    message = await update.reply_text(text="`Processing...`")
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    try:
        limit = int(message.text)
    except:
        await message.edit_text('Limit is wrong')
        return
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nJoin @mwpro11",
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Movie World', url='https://t.me/mwmoviespro')]])
    await message.edit_text(text, True)	

#Share Text

def share_link(text: str) -> str:
    return "**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(text)

@Client.on_message(filters.command(["share", "sharetext", "st", "stxt", "shtxt", "shtext"]))
async def share_text(client, message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1. Reply Any Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Support Chat", url=f"https://t.me/{SUPPORT_CHAT}")
                    ]                
                ]
            ),
            reply_to_message_id=reply_id
        )
        return
    await message.reply_text(share_link(input_text), reply_to_message_id=reply_id)

#TTS

def convert(text):
    audio = BytesIO()
    i = Translator().translate(text, dest="en")
    lang = i.src
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".mp3"
    tts.write_to_fp(audio)
    return audio

@Client.on_message(filters.command("tts"))
async def text_to_speech(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to some text ffs.")
    if not message.reply_to_message.text:
        return await message.reply_text("Reply to some text ffs.")
    m = await message.reply_text("Processing")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(e)
        e = traceback.format_exc()
        print(e)

#Telegraph

@Client.on_message(filters.command(["tgmedia", "tgraph", "telegraph"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"<b>Link:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="『𝕺𝙿𝙴𝙽 𝕷𝙸𝙽𝙺』", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="『𝕾𝙷𝙰𝚁𝙴 𝕷𝙸𝙽𝙺』", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
             ], [
                InlineKeyboardButton(text="『𝙿𝚁𝙴𝚅』", callback_data="close_data")
           ]]
        )
    )
    finally:
        os.remove(download_location)

@Client.on_message(filters.command('whois') & f_onw_fliter)
async def who_is(client, message):
    """ extract user information """
    status_message = await message.reply_text(
        "നിക്കു നെൻപ നോക്കട്ടെ 🙂"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        await status_message.edit("no valid user_id / message specified")
        return
    
    first_name = from_user.first_name or ""
    last_name = from_user.last_name or ""
    username = from_user.username or ""
    
    message_out_str = (
        "<b>Name:</b> "
        f"<a href='tg://user?id={from_user.id}'>{first_name}</a>\n"
        f"<b>Suffix:</b> {last_name}\n"
        f"<b>Username:</b> @{username}\n"
        f"<b>User ID:</b> <code>{from_user.id}</code>\n"
        f"<b>User Link:</b> {from_user.mention}\n" if from_user.username else ""
        f"<b>Is Deleted:</b> True\n" if from_user.is_deleted else ""
        f"<b>Is Verified:</b> True" if from_user.is_verified else ""
        f"<b>Is Scam:</b> True" if from_user.is_scam else ""
        # f"<b>Is Fake:</b> True" if from_user.is_fake else ""
        f"<b>Last Seen:</b> <code>{last_online(from_user)}</code>\n\n"
    )

    if message.chat.type in ["supergroup", "channel"]:
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>Joined on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            caption=message_out_str,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        await message.reply_text(
            text=message_out_str,
            quote=True,
            disable_notification=True
        )
    await status_message.delete()
