from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import enums
from info import DATABASE_URI, DATABASE_NAME
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]


async def add_filter(grp_id, text, reply_text, btn, file, alert):
    mycol = db[str(grp_id)]

    data = {
        "text": str(text),
        "reply": str(reply_text),
        "btn": str(btn),
        "file": str(file),
        "alert": str(alert),
    }

    try:
        await mycol.update_one({"text": str(text)}, {"$set": data}, upsert=True)
    except Exception as e:
        logger.exception(f"Some error occurred! {e}", exc_info=True)


async def find_filter(group_id, name):
    mycol = db[str(group_id)]

    try:
        file = await mycol.find_one({"text": name})
        if not file:
            return None, None, None, None

        reply_text = file.get("reply")
        btn = file.get("btn")
        fileid = file.get("file")
        alert = file.get("alert", None)

        return reply_text, btn, alert, fileid
    except Exception as e:
        logger.exception(f"Error finding filter: {e}", exc_info=True)
        return None, None, None, None


async def get_filters(group_id):
    mycol = db[str(group_id)]
    texts = []
    try:
        async for file in mycol.find():
            texts.append(file["text"])
    except Exception as e:
        logger.exception(f"Error getting filters: {e}", exc_info=True)
    return texts


async def delete_filter(message, text, group_id):
    mycol = db[str(group_id)]
    query = {"text": text}
    count = await mycol.count_documents(query)

    if count == 1:
        await mycol.delete_one(query)
        await message.reply_text(
            f"`{text}` deleted. I'll not respond to that filter anymore.",
            quote=True,
            parse_mode=enums.ParseMode.MARKDOWN,
        )
    else:
        await message.reply_text("Couldn't find that filter!", quote=True)


async def del_all(message, group_id, title):
    if str(group_id) not in await db.list_collection_names():
        await message.edit_text(f"Nothing to remove in {title}!")
        return

    try:
        await db.drop_collection(str(group_id))
        await message.edit_text(f"All filters from {title} have been removed")
    except Exception as e:
        await message.edit_text("Couldn't remove all filters from group!")
        logger.exception(f"Error deleting all filters: {e}", exc_info=True)


async def count_filters(group_id):
    mycol = db[str(group_id)]
    count = await mycol.count_documents({})
    return False if count == 0 else count


async def filter_stats():
    collections = await db.list_collection_names()

    if "CONNECTION" in collections:
        collections.remove("CONNECTION")

    totalcount = 0
    for collection in collections:
        mycol = db[collection]
        count = await mycol.count_documents({})
        totalcount += count

    totalcollections = len(collections)

    return totalcollections, totalcount
