import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("ππ­π°π΄π¦", callback_data='close_data')]])

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
β π²ππππππ’     : `{country}`
β π°ππππππ     : `{active}`
β π²ππππππππ   : `{confirmed}`
β π³πππππ      : `{deaths}`
β πΈπ³          : `{info_id}`
β π»πππ ππππππ : `{last_update}`
β π»ππππππe    : `{latitude}`
β π»ππππππππ   : `{longitude}`
β πππππππππ   : `{recovered}`"""
        return covid_info
    except Exception as error:
        return error
