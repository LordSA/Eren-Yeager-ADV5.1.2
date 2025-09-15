'''import os
import subprocess
from pyrogram import Client, filters
from pyrogram.types import Message
from info import AUTH_USERS, LOG_CHANNEL   # AUTH_USERS = [owner_id], LOG_CHANNEL = -100xxxxxxxxxx


OWNER_ID = AUTH_USERS if isinstance(AUTH_USERS, int) else AUTH_USERS[0]


def set_env_var(key: str, value: str):
    """Set environment variable and persist with pm2"""
    os.environ[key] = value
    subprocess.run(["pm2", "set", key, value])


def get_env_var(key: str):
    """Get environment variable"""
    return os.environ.get(key)


def del_env_var(key: str):
    """Delete environment variable"""
    os.environ.pop(key, None)
    subprocess.run(["pm2", "unset", key])


async def send_log(client: Client, text: str):
    """Send logs to LOG_CHANNEL safely"""
    try:
        if LOG_CHANNEL:
            await client.send_message(LOG_CHANNEL, text)
    except Exception as e:
        print(f"[LOG ERROR] {e}")


@Client.on_message(filters.command("setvar") & filters.user(OWNER_ID))
async def set_variable(client: Client, message: Message):
    if len(message.command) < 3:
        return await client.send_message(
            OWNER_ID, "⚠️ Usage: <code>/setvar VAR_NAME value</code>"
        )

    key = message.command[1]
    value = " ".join(message.command[2:])

    set_env_var(key, value)
    msg = f"✅ Environment variable <b>{key}</b> set to:\n<code>{value}</code>"
    await client.send_message(OWNER_ID, msg)
    await send_log(client, f"📝 [SETVAR]\nOwner set `{key}` = `{value}`")


@Client.on_message(filters.command("getvar") & filters.user(OWNER_ID))
async def get_variable(client: Client, message: Message):
    if len(message.command) != 2:
        return await client.send_message(
            OWNER_ID, "⚠️ Usage: <code>/getvar VAR_NAME</code>"
        )

    key = message.command[1]
    value = get_env_var(key)

    if value is None:
        msg = f"❌ Environment variable <b>{key}</b> not found."
    else:
        msg = f"🔑 <b>{key}</b> = <code>{value}</code>"

    await client.send_message(OWNER_ID, msg)
    await send_log(client, f"🔎 [GETVAR]\n{msg}")


@Client.on_message(filters.command("delvar") & filters.user(OWNER_ID))
async def delete_variable(client: Client, message: Message):
    if len(message.command) != 2:
        return await client.send_message(
            OWNER_ID, "⚠️ Usage: <code>/delvar VAR_NAME</code>"
        )

    key = message.command[1]
    if get_env_var(key) is None:
        msg = f"❌ Environment variable <b>{key}</b> not found."
        await client.send_message(OWNER_ID, msg)
        await send_log(client, f"⚠️ [DELVAR]\n{msg}")
        return

    del_env_var(key)
    msg = f"🗑️ Environment variable <b>{key}</b> deleted."
    await client.send_message(OWNER_ID, msg)
    await send_log(client, f"🗑️ [DELVAR]\n{msg}")'''
