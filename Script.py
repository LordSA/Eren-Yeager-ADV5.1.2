class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍,
© 𝙴𝚛𝚎𝚗 𝚈𝚎𝚊𝚐𝚎𝚛 💖
© <a href =https://t.me/lord1of5darkness9>𝕷𝖔𝖗𝖉 𝖔𝖋 𝕯𝖆𝖗𝖐𝖓𝖊𝖘𝖘</a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/mwpro11>𝕷𝖔𝖗𝖉 𝖔𝖋 𝕯𝖆𝖗𝖐𝖓𝖊𝖘𝖘</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href=https://docs.pyrogram.org/>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: <a href=https://www.python.org/>𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</a>
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: <a href=https://www.mongodb.com/>𝙼𝙾𝙽𝙶𝙾 𝙳𝙱</a>
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: <a href=https://id.heroku.com/login>𝙷𝙴𝚁𝙾𝙺𝚄</a>
✯ 𝙲𝙾𝙳𝙴𝙳 𝙱𝚈: <a href=https://github.com/LordSA>𝙻𝙾𝚁𝙳 𝚂𝙰</a>
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v5.2.1 [ 𝙱𝙴𝚃𝙰 ]
⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸"""
    SOURCE_TXT = """<b>NOTE:</b>
✯ 🄼🄾🅅🄸🄴 🅆🄾🅁🄻🄳 🄸🅂 🄰 🄾🄿🄴🄽 🅂🄾🅄🅁🄲🄴 🄿🅁🄾🄹🄴🄲🅃. 
✯ 𝚂𝙾𝚄𝚁𝙲𝙴 - <a href=https://t.me/lord1of5darkness9>𝙴𝚁𝙴𝙽 𝚈𝙴𝙰𝙶𝙴𝚁💔</a>  

<b>𝔇𝔢𝔳𝔢𝔩𝔬𝔭𝔢𝔯:</b>
- <a href=https://t.me/mwpro11>𝕷𝖔𝖗𝖉 𝖔𝖋 𝕯𝖆𝖗𝖐𝖓𝖊𝖘𝖘</a>"""
    WHOIS_TXT ="""<b>ᴡʜᴏɪs ᴍᴏᴅᴜʟᴇ</b>
ɴᴏᴛᴇ:- ɢɪᴠᴇ ᴀ ᴜsᴇʀ ᴅᴇᴛᴀɪʟs
•/whois : ɢɪᴠᴇ ᴀ ᴜsᴇʀ 𝔉ᴜʟʟ ᴅᴇᴛᴀɪʟs"""
    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>𝙵𝙸𝙻𝚃𝙴𝚁𝚂</b>

✯ ғɪʟᴛᴇʀ ɪs 🅃🄷🄴 🄵🄴🄰🅃🅄🅁🄴 🅆🄴🅁🄴 🅄🅂🄴🅁🅂 🄲🄰🄽 🅂🄴🅃 🄰🅄🅃🄾🄼🄰🅃🄴🄳 🅁🄴🄿🄻🄸🄴🅂 🄵🄾🅁 🄰 🄿🄰🅁🅃🄸🄲🅄🄻🄰🅁 🄺🄴🅈🅆🄾🅁🄳 🄰🄽🄳 🄼🄾🅅🄸🄴 🅆🄾🅁🄻🄳 🅆🄸🄻🄻 🅁🄴🅂🄿🄾🄽🄳 🅆🄷🄴🄽🄴🅅🄴🅁 🄰 🄺🄴🅈🅆🄾🅁🄳 🄸🅂 🄵🄾🅄🄽🄳 🅃🄷🄴 🄼🄴🅂🅂🄰🄶🄴

<b>ɴᴏᴛᴇ:</b>
1. ᴇʀᴇɴ ʏᴇᴀɢᴇʀ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• /filter - <code>ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ [ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ]</code>"""
    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴs</b>

- Movie World Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Movie World supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mwpro2_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Movie World

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
• /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    TGRAPH_TXT = """Help: <b>TELEGRAPH & PASTE</b>

<b>NOTE:</b>
• IMDb should have admin privillage
• These commands works on both pm and group
• These commands can be used by any group member

<b>Commands and Usage:</b>

• /tgmedia or /tgraph - <code>upload supported media (within 5MB) to telegraph.</code>"""
    STICKER_TXT = """𝙃𝙚𝙡𝙥 𝙁𝙤𝙧 𝙎𝙩𝙞𝙘𝙠𝙚𝙧 𝙄𝙙
    
• 𝙐𝙨𝙖𝙜𝙚

To Get Sticker ID
 
 ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
  
◉ Reply To Any Sticker [/stickerid]"""
    RESTRIC_TXT = """Help: <b>Restrictions</b>

<b>What is this?</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""
    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
• /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
• /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works only group.
• These commands can be used by Only admin."""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    OTH_TXT = """EXTRA BUTTONS FOR USE...."""
    FILT_TXT = """ALL FILTER BUTTONS ARE HERE"""
    MANEGER_TXT = """Do You Think I can Manage Your Group Then Don't Think Use My Features"""
    TEXTWORK_TXT = """Text Editing and Link Editing or Regeneration"""
    PINGS_TXT ="""<b>🌟 Ping:</b>
Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /help - To get help 
• /ping - To get your ping 
• /repo - Source Code.

<b>🏹Usage🏹 :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
    TORRENT_TXT = """<b>Torrent Search</b>

<b>Commands and Usage:</b>
• /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    MEMES_TXT = """Help: <b>FUN</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
• /throw or /dart - t𝗈 m𝖺𝗄𝖾 drat 
• /roll or /dice - roll the dice 
• /goal or /shoot - to make a goal or shoot
• /luck or /cownd - Spin the Lucky
• /runs strings

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    INFO_TXT = """Help: <b>Json</b>

<b>Commands and Usage:</b>
• /json - <code>get the json details of a message.<code>
<code> /id & /info is not from json it's just added to this.<code>

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
• /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
• /song or /mp3 (songname) - download song from yt servers.
• /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
• /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
• /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

a bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
• /share (text or reply to message)

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""

    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
