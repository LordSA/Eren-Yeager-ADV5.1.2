from motor.motor_asyncio import AsyncIOMotorClient
from info import DATABASE_URI, DATABASE_NAME
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
mycol = db["USER"]


async def insert(chat_id: int):
    user_det = {"_id": int(chat_id), "lg_code": None}
    try:
        await mycol.insert_one(user_det)
    except Exception as e:
        logger.debug(f"User already exists or error: {e}")


async def set(chat_id: int, lg_code: str):
    await mycol.update_one({"_id": chat_id}, {"$set": {"lg_code": lg_code}}, upsert=True)


async def unset(chat_id: int):
    await mycol.update_one({"_id": chat_id}, {"$set": {"lg_code": None}})


async def find(chat_id: int):
    doc = await mycol.find_one({"_id": chat_id}, {"lg_code": 1})
    return doc["lg_code"] if doc else None


async def getid():
    values = []
    async for key in mycol.find({}, {"_id": 1}):
        values.append(key["_id"])
    return values


async def find_one(id: int):
    return await mycol.find_one({"_id": id})
