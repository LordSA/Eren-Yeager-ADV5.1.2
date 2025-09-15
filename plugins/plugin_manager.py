import os
import re
import sys
import aiohttp
import importlib.util
from pyrogram import Client, filters
from info import ADMINS, LOG_CHANNEL
from plugin_db import PluginDB, install_plugin  # Your MongoDB plugin setup

OWNER_ID = ADMINS if isinstance(ADMINS, list) else [ADMINS]

# ------------------- Helpers -------------------
async def fetch_url(url: str) -> str | None:
    """Fetch plugin code from a URL"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url + f"?timestamp={int(__import__('time').time())}") as resp:
                if resp.status == 200:
                    return await resp.text()
                return None
    except Exception as e:
        print(f"[ERROR] Failed to fetch URL: {e}")
        return None

def load_plugin(plugin_name: str):
    """Dynamically load a plugin from plugins/ folder"""
    os.makedirs("plugins", exist_ok=True)
    init_file = os.path.join("plugins", "__init__.py")
    if not os.path.exists(init_file):
        open(init_file, "w").close()

    file_path = os.path.join("plugins", f"{plugin_name}.py")
    if not os.path.exists(file_path):
        return None

    try:
        spec = importlib.util.spec_from_file_location(f"plugins.{plugin_name}", file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[f"plugins.{plugin_name}"] = module
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"[ERROR] Loading plugin {plugin_name}: {e}")
        if f"plugins.{plugin_name}" in sys.modules:
            del sys.modules[f"plugins.{plugin_name}"]
        return None

# ------------------- INSTALL PLUGIN -------------------
@Client.on_message(filters.command("pinstall") & filters.user(OWNER_ID))
async def install_plugin_cmd(client, message):
    text = " ".join(message.command[1:]) or (message.reply_to_message.text if message.reply_to_message else None)
    if not text:
        return await message.reply("❌ Provide a plugin URL")

    urls = re.findall(r'https?://\S+', text)
    if not urls:
        return await message.reply("❌ No valid URL found")

    for url in urls:
        if "gist.github.com" in url and not url.endswith("raw"):
            url = url.rstrip("/") + "/raw"

        code = await fetch_url(url)
        if not code:
            await message.reply(f"❌ Failed to fetch plugin: {url}")
            continue

        plugin_name_match = re.search(r'pattern:\s*["\'](.*?)["\']', code)
        plugin_name = plugin_name_match.group(1).split()[0] if plugin_name_match else f"plugin_{int(__import__('time').time())}"

        file_path = os.path.join("plugins", f"{plugin_name}.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

        if not load_plugin(plugin_name):
            os.remove(file_path)
            await message.reply(f"❌ Invalid plugin: {plugin_name}")
            continue

        await install_plugin(url, plugin_name)
        await message.reply(f"✅ Installed plugin: {plugin_name}")

# ------------------- LIST PLUGINS -------------------
@Client.on_message(filters.command("plugin") & filters.user(OWNER_ID))
async def list_plugins_cmd(client, message):
    plugins = await PluginDB.find_all()
    if not plugins:
        return await message.reply("No plugins installed")

    text = "Installed plugins:\n\n"
    for p in plugins:
        text += f"• {p['name']} : {p['url']}\n"
    await message.reply(text)

# ------------------- REMOVE PLUGIN -------------------
@Client.on_message(filters.command("premove") & filters.user(OWNER_ID))
async def remove_plugin_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Specify plugin name")
    plugin_name = message.command[1]

    plugin = await PluginDB.find_by_name(plugin_name)
    if not plugin:
        return await message.reply("❌ Plugin not found")

    await PluginDB.remove(plugin_name)

    file_path = os.path.join("plugins", f"{plugin_name}.py")
    if os.path.exists(file_path):
        os.remove(file_path)
    sys.modules.pop(f"plugins.{plugin_name}", None)

    await message.reply(f"🗑️ Removed plugin: {plugin_name}")

# ------------------- UPDATE PLUGIN -------------------
@Client.on_message(filters.command("pupdate") & filters.user(OWNER_ID))
async def update_plugin_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Specify plugin name")
    plugin_name = message.command[1]

    plugin = await PluginDB.find_by_name(plugin_name)
    if not plugin:
        return await message.reply("❌ Plugin not found")

    code = await fetch_url(plugin["url"])
    if not code:
        return await message.reply("❌ Failed to fetch plugin")

    file_path = os.path.join("plugins", f"{plugin_name}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

    if not load_plugin(plugin_name):
        os.remove(file_path)
        await message.reply(f"❌ Invalid plugin after update: {plugin_name}")
        return

    await message.reply(f"✅ Updated plugin: {plugin_name}")
