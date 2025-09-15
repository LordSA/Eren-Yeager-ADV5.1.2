import os
import re
import sys
import aiohttp
import importlib.util
from pyrogram import Client, filters
from info import ADMINS, LOG_CHANNEL
from plugin_db import PluginDB, install_plugin  # MongoDB setup

OWNER_ID = 1125789849 #ADMINS

# ------------------- Helpers -------------------
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + f"?timestamp={int(__import__('time').time())}") as resp:
            if resp.status == 200:
                return await resp.text()
            return None

def load_plugin(plugin_name):
    """Dynamically load plugin from plugins/ folder"""
    os.makedirs("plugins", exist_ok=True)
    file_path = os.path.join("plugins", f"{plugin_name}.py")
    if not os.path.exists(file_path):
        return None
    spec = importlib.util.spec_from_file_location(plugin_name, file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules[plugin_name] = module
        spec.loader.exec_module(module)
        return module
    return None

# ------------------- INSTALL PLUGIN -------------------
@Client.on_message(filters.command("pinstall") & filters.user(OWNER_ID))
async def install_plugin_cmd(client, message):
    match = " ".join(message.command[1:]) or (message.reply_to_message.text if message.reply_to_message else None)
    if not match or not re.findall(r'\bhttps?://\S+', match):
        return await message.reply("❌ Please provide a valid URL")
    
    links = re.findall(r'\bhttps?://\S+', match)
    for link in links:
        if "gist.github.com" in link:
            link = link if link.endswith("raw") else link + "/raw"

        data = await fetch_url(link)
        if not data:
            return await message.reply("❌ Invalid URL or failed to fetch plugin")
        
        plugin_name_match = re.search(r'pattern:\s*["\'](.*?)["\']', data)
        plugin_name = plugin_name_match.group(1).split()[0] if plugin_name_match else "temp_plugin"

        file_path = os.path.join("plugins", f"{plugin_name}.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data)

        try:
            load_plugin(plugin_name)
        except Exception as e:
            os.remove(file_path)
            return await message.reply(f"❌ Invalid plugin: {e}")
        
        await install_plugin(link, plugin_name)
        await message.reply(f"✅ Installed plugin: {plugin_name}")

# ------------------- LIST PLUGINS -------------------
@Client.on_message(filters.command("plugin") & filters.user(OWNER_ID))
async def list_plugins_cmd(client, message):
    match = " ".join(message.command[1:])
    plugins = await PluginDB.find_all()
    
    if match:
        plugin = next((p for p in plugins if p["name"] == match), None)
        if plugin:
            return await message.reply(f"🔗 {plugin['name']}: {plugin['url']}")
        return await message.reply("❌ Plugin not found")
    
    if not plugins:
        return await message.reply("No plugins installed")
    
    msg = "Installed plugins:\n\n"
    for p in plugins:
        msg += f"• {p['name']} : {p['url']}\n"
    await message.reply(msg)

# ------------------- REMOVE PLUGIN -------------------
@Client.on_message(filters.command("premove") & filters.user(OWNER_ID))
async def remove_plugin_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Specify plugin name to remove")
    plugin_name = message.command[1]
    plugin = await PluginDB.find_by_name(plugin_name)
    if not plugin:
        return await message.reply("❌ Plugin not found")
    
    await PluginDB.remove(plugin_name)
    try:
        file_path = os.path.join("plugins", f"{plugin_name}.py")
        if os.path.exists(file_path):
            os.remove(file_path)
        if plugin_name in sys.modules:
            del sys.modules[plugin_name]
    except: pass
    await message.reply(f"🗑️ Deleted plugin: {plugin_name}")

# ------------------- UPDATE PLUGIN -------------------
@Client.on_message(filters.command("pupdate") & filters.user(OWNER_ID))
async def update_plugin_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Specify plugin name to update")
    plugin_name = message.command[1]
    plugin = await PluginDB.find_by_name(plugin_name)
    if not plugin:
        return await message.reply("❌ Plugin not found")
    
    data = await fetch_url(plugin["url"])
    if not data:
        return await message.reply("❌ Failed to fetch plugin")
    
    file_path = os.path.join("plugins", f"{plugin_name}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data)
    
    try:
        load_plugin(plugin_name)
    except Exception as e:
        os.remove(file_path)
        return await message.reply(f"❌ Invalid plugin after update: {e}")
    
    await message.reply(f"✅ Updated plugin: {plugin_name}")
