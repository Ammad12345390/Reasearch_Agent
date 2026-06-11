from datetime import datetime, timezone

from app.database import db


async def save_log(data: dict):
    """
    Save agent execution logs to MongoDB.
    """

    log_document = {
        "user_id": data.get("user_id"),
        "topic": data.get("topic"),
        "summary": data.get("summary"),
        "execution_time": data.get("execution_time"),
        "timestamp": datetime.now(timezone.utc),
    }

    result = await db.agent_logs.insert_one(log_document)

    return {
        "message": "Log saved successfully",
        "inserted_id": str(result.inserted_id),
    }