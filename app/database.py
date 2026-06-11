import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGODB_URL)

db = client[DATABASE_NAME]

agent_logs_collection = db["agent_logs"]


async def save_agent_log(
    user_id: str,
    topic: str,
    summary: str,
    execution_time: float,
):
    document = {
        "user_id": user_id,
        "topic": topic,
        "summary": summary,
        "execution_time": execution_time,
        "timestamp": datetime.now(timezone.utc),
    }

    result = await agent_logs_collection.insert_one(document)

    return str(result.inserted_id)