from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["country"]))
async def country_info(update: Message):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""--**𝙲𝙾𝚄𝙽𝚃𝚁𝚈 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽**--

『𝙽𝙰𝙼𝙴』 : `{country.name()}`
『𝙽𝙰𝚃𝙸𝚅𝙴 𝙽𝙰𝙼𝙴』 : `{country.native_name()}`
『𝙲𝙰𝙿𝙸𝚃𝙰𝙻』 : `{country.capital()}`
『𝙿𝙾𝙿𝚄𝙻𝙰𝚃𝙸𝙾𝙽』 : `{country.population()}`
『𝚁𝙴𝙶𝙸𝙾𝙽』 : `{country.region()}`
『𝚂𝚄𝙱 𝚁𝙴𝙶𝙸𝙾𝙽』 : `{country.subregion()}`
『𝚃𝙾𝙿 𝙻𝙴𝚅𝙴𝙻 𝙳𝙾𝙼𝙰𝙸𝙽𝚂』 : `{country.tld()}`
『𝙲𝙰𝙻𝙻𝙸𝙽𝙶 𝙲𝙾𝙳𝙴』 : `{country.calling_codes()}`
『𝙲𝚄𝚁𝚁𝙴𝙽𝙲𝚈』 : `{country.currencies()}`
『𝚁𝙴𝚂𝙸𝙳𝙴𝙽𝙲𝙴』 : `{country.demonym()}`
『𝚃𝙸𝙼𝙴𝚉𝙾𝙽𝙴』 : `{country.timezones()}`

 **@mwpro11**"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('『𝚆𝙸𝙺𝙸𝙿𝙴𝙳𝙸𝙰』', url=f'{country.wiki()}'),
        InlineKeyboardButton('『𝙶𝙾𝙾𝙶𝙻𝙴』', url=f'https://www.google.com/search?q={country_name}')
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
