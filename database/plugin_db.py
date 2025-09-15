import os
from motor.motor_asyncio import AsyncIOMotorClient
from info import DATABASE_URI, DATABASE_NAME

# Connect to MongoDB
client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
plugin_collection = db['plugins']

class PluginDB:
    @staticmethod
    async def add(name: str, url: str):
        """Add a plugin if it doesn't exist"""
        exists = await plugin_collection.find_one({"name": name})
        if exists:
            return exists
        plugin = {"name": name, "url": url}
        await plugin_collection.insert_one(plugin)
        return plugin

    @staticmethod
    async def find_all():
        """Return a list of all installed plugins"""
        plugins = await plugin_collection.find({}).to_list(length=1000)
        return plugins

    @staticmethod
    async def find_by_name(name: str):
        """Get plugin details by name"""
        return await plugin_collection.find_one({"name": name})

    @staticmethod
    async def remove(name: str):
        """Remove plugin by name"""
        plugin = await plugin_collection.find_one({"name": name})
        if plugin:
            await plugin_collection.delete_one({"name": name})
        return plugin

async def install_plugin(url: str, name: str):
    """Helper function to add plugin to DB"""
    plugin = await PluginDB.find_by_name(name)
    if plugin:
        return plugin
    return await PluginDB.add(name, url)
