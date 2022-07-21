from pyrogram import Client, filters
from plugins.Tools.help_func.admin_check import admin_check
from plugins.Tools.help_func.extract_user import extract_user


@Client.on_message(filters.command(["gunban", "gunmute"]))
async def un_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.unban_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "നിന്നേ വെറുതെ വിട്ടു "
                f"{user_first_name} To "
                " നിനക്ക് ഇനി ഗ്രൂപ്പിൽ കേറാം!"
            )
        else:
            await message.reply_text(
                "നിന്നേ വെറുതെ വിട്ടു "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> To "
                " നിനക്ക് ഇനി ഗ്രൂപ്പിൽ കേറാം!"
            )
