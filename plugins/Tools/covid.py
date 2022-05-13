import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("𝘊𝘭𝘰𝘴𝘦", callback_data='close_data')]])

@Client.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo="https://telegra.ph/file/2f96302d507dbda5126f0.jpg",
        caption=covid_info(query),
        quote=True
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Covid 19 Information**--
⟁ 𝙲𝚘𝚞𝚗𝚝𝚛𝚢     : `{country}`
⟁ 𝙰𝚌𝚝𝚒𝚟𝚎𝚍     : `{active}`
⟁ 𝙲𝚘𝚗𝚏𝚒𝚛𝚖𝚎𝚍   : `{confirmed}`
⟁ 𝙳𝚎𝚊𝚝𝚑𝚜      : `{deaths}`
⟁ 𝙸𝙳          : `{info_id}`
⟁ 𝙻𝚊𝚜𝚝 𝚄𝚙𝚍𝚊𝚝𝚎 : `{last_update}`
⟁ 𝙻𝚊𝚝𝚒𝚝𝚞𝚍e    : `{latitude}`
⟁ 𝙻𝚘𝚗𝚐𝚒𝚝𝚞𝚍𝚎   : `{longitude}`
⟁ 𝚁𝚎𝚌𝚘𝚟𝚎𝚛𝚎𝚍   : `{recovered}`"""
        return covid_info
    except Exception as error:
        return error
