![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=WELCOME+TO+MY+DOMAIN!;MY+NAME+IS+EREN+YEAGER;I'M+A+POWERFUL+MOVIE+USERBOT;WITH+ULTRA+FEATURES!)

<p align="center">
  <img src="https://telegra.ph/file/7226c9d57dc698158bab2.jpg" alt="Eren Yeager Logo">
</p>

# 𝙴𝚁𝙴𝙽 𝚈𝙴𝙰𝙶𝙴𝚁 ADV5.2.0

[![Stars](https://img.shields.io/github/stars/LordSA/movie-world?style=flat-square&color=yellow)](https://github.com/LordSA/movie-world/stargazers)  
[![Forks](https://img.shields.io/github/forks/LordSA/movie-world?style=flat-square&color=orange)](https://github.com/LordSA/movie-world/fork)  
[![Size](https://img.shields.io/github/repo-size/LordSA/movie-world?style=flat-square&color=green)](https://github.com/LordSA/movie-world/)  
[![Contributors](https://img.shields.io/github/contributors/LordSA/movie-world?style=flat-square&color=green)](https://github.com/LordSA/movie-world/graphs/contributors)  
[![License](https://img.shields.io/badge/License-AGPLv3-blue)](https://www.gnu.org/licenses/agpl-3.0.en.html)  

---

## Features
- Auto Filter & Manual Filter  
- IMDB Search & Info  
- Admin Commands  
- Broadcast & Stats  
- Inline Search  
- Random Pics  
- User & Chat Info  
- Spell Check  
- Index & Manage Files  

---

## Variables
### Required
- `BOT_TOKEN` — Bot token from [@BotFather](https://telegram.dog/BotFather)  
- `API_ID` & `API_HASH` — From [my.telegram.org](https://my.telegram.org/apps)  
- `CHANNELS` — Channels or groups (space-separated)  
- `ADMINS` — Admins (space-separated)  
- `DATABASE_URI` & `DATABASE_NAME` — MongoDB URI & database name  
- `LOG_CHANNEL` — Channel for logs  

### Optional
- `PICS` — Telegraph links of images for start messages (space-separated)  
> Check `info.py` for examples and defaults

---

## Deploy

<details><summary>Deploy To VPS</summary>
  
```bash
git clone https://github.com/LordSA/EREN-YEAGER-ADV5.2.0.git
cd /EREN-YEAGER-ADV5.2.0
```

# Install Packages
````
pip3 install U -r requirements.txt
````
Edit info.py with variables as given below then run bot(to test)
````
python3 bot.py
````
then
````
pm2 start venv/bin/python3 --name eren-bot -- bot.py
pm2 logs eren-bot
````
</details>


## Commands
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /connections - view the connections
* /settings - settings for connected groups
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
* /imdb - fetch info from imdb.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
* /enable - re-enable chat.
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all Eva Maria users
```

---

## Support
[![OWNER](https://img.shields.io/badge/Telegram-Group-30302f?style=flat&logo=telegram)](https://telegram.dog/shibili_offline)  
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-30302f?style=flat&logo=telegram)](https://telegram.dog/mwpro11)

---

## Credits
- Dan — [Pyrogram Library](https://github.com/pyrogram/pyrogram)  
- Mahesh — [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)  
- Trojanz — [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) & [AutoFilterBot](https://github.com/trojanzhex/auto-filter-bot)
- Subin for the Evamaria [Evamaria](https://github.com/EvamariaTG/Evamaria)  
- Everyone who supported this project

---

### Note
Forking, editing a few lines, or releasing a branch doesn’t make you the original developer. Fork the repo and edit as per your needs.

---

## Disclaimer
Licensed under [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html#header).  
Selling this code for money is *strictly prohibited*.
