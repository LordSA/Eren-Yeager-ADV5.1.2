import logging
import logging.config
import subprocess
from pyrogram import filters
from pyrogram.types import Message
from info import LOG_CHANNEL, AUTH_USERS

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types

class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")
    
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1


app = Bot()
OWNER_ID = AUTH_USERS  

@app.on_message(filters.command("update") & filters.user(OWNER_ID))
async def update_bot(client: Client, message: Message):
    owner = message.from_user.id

    # Notify owner DM
    await client.send_message(owner, "🚀 Update started...")

    # Step 1: Git Pull
    git_pull = subprocess.run(["git", "pull"], capture_output=True, text=True)
    git_output = git_pull.stdout + git_pull.stderr

    if "Already up to date." in git_output:
        await client.send_message(owner, "✅ Bot is already up-to-date.")
        return

    await client.send_message(LOG_CHANNEL, f"📦 <b>Git Pull Logs</b>:\n<code>{git_output}</code>")

    # Step 2: Install requirements
    pip_install = subprocess.run(["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True)
    pip_output = pip_install.stdout + pip_install.stderr

    await client.send_message(LOG_CHANNEL, f"📦 <b>Pip Install Logs</b>:\n<code>{pip_output}</code>")

    # Step 3: Restart bot with PM2
    subprocess.run(["pm2", "restart", "eren-bot"])

    # Final DM to owner
    await client.send_message(owner, "✅ Update finished. Bot restarted successfully!")
    '''
    async def send_log(client, text: str):
    try:
        if LOG_CHANNEL:
            await client.send_message(LOG_CHANNEL, text)
    except Exception as e:
        print(f"[LOG ERROR] {e}")


@Client.on_message(filters.command("update") & filters.user(AUTH_USERS))
async def update_bot(client: Client, message: Message):
    owner_id = message.from_user.id

    # DM only
    await client.send_message(owner_id, "🚀 Update started...")

    # Step 1: Git Pull
    git_pull = subprocess.run(["git", "pull"], capture_output=True, text=True)
    git_output = git_pull.stdout + git_pull.stderr

    if "Already up to date." in git_output:
        await client.send_message(owner_id, "✅ Bot is already up to date.")
        return

    await client.send_message(owner_id, f"📦 Git Pull Output:\n{git_output}")
    await send_log(client, "📥 New update pulled from GitHub.")

    # Step 2: Install requirements
    pip_install = subprocess.run(
        ["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True
    )
    pip_output = pip_install.stdout + pip_install.stderr
    await client.send_message(owner_id, f"📦 Requirements:\n{pip_output}")

    # Step 3: Restart bot
    subprocess.run(["pm2", "restart", "eren-bot"])
    await client.send_message(owner_id, "✅ Update completed & bot restarted.")
    await send_log(client, "♻️ Bot restarted after update.")'''
app.run()


