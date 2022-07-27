from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["country"]))
async def country_info(update: Message):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""--**Country Information**--

『𝙿𝚁𝙴𝚅』 : `{country.name()}`
Native Name『𝙿𝚁𝙴𝚅』 : `{country.native_name()}`
Capital『𝙿𝚁𝙴𝚅』 : `{country.capital()}`
Population『𝙿𝚁𝙴𝚅』 : `{country.population()}`
Region『𝙿𝚁𝙴𝚅』 : `{country.region()}`
Sub Region『𝙿𝚁𝙴𝚅』 : `{country.subregion()}`
Top Level Domains『𝙿𝚁𝙴𝚅』 : `{country.tld()}`
Calling Codes『𝙿𝚁𝙴𝚅』 : `{country.calling_codes()}`
Currencies『𝙿𝚁𝙴𝚅』 : `{country.currencies()}`
Residence『𝙿𝚁𝙴𝚅』 : `{country.demonym()}`
Timezone『𝙿𝚁𝙴𝚅』 : `{country.timezones()}`

Made by **@mwpro11**"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia『𝙿𝚁𝙴𝚅』', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google『𝙿𝚁𝙴𝚅』', url=f'https://www.google.com/search?q={country_name}')
        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
