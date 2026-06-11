import asyncio
import time
from datetime import datetime, timezone
from typing import TypedDict

from fastapi import FastAPI, HTTPException
from langgraph.graph import END, StateGraph
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field


app = FastAPI(title="Research Summarizer Agent API")


client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["agent_db"]
agent_logs = db["agent_logs"]


class TopicRequest(BaseModel):
    topic: str = Field(..., min_length=3, max_length=200)
    user_id: str = Field(..., min_length=1, max_length=100)


class TopicResponse(BaseModel):
    summary: str
    execution_time: float


class AgentState(TypedDict):
    topic: str
    facts: str
    summary: str


async def researcher(state: AgentState):
    await asyncio.sleep(1)

    return {
        "facts": f"Important facts about {state['topic']}"
    }


async def summarizer(state: AgentState):
    await asyncio.sleep(1)

    return {
        "summary": f"Short summary of {state['facts']}"
    }


graph = StateGraph(AgentState)

graph.add_node("researcher", researcher)
graph.add_node("summarizer", summarizer)

graph.set_entry_point("researcher")
graph.add_edge("researcher", "summarizer")
graph.add_edge("summarizer", END)

workflow = graph.compile()


@app.get("/")
async def root():
    return {
        "message": "FastAPI LangGraph MongoDB Agent is running"
    }


@app.post("/generate-summary", response_model=TopicResponse)
async def generate_summary(request: TopicRequest):
    start_time = time.perf_counter()

    try:
        result = await workflow.ainvoke(
            {
                "topic": request.topic,
                "facts": "",
                "summary": "",
            }
        )

        execution_time = round(time.perf_counter() - start_time, 2)

        await agent_logs.insert_one(
            {
                "user_id": request.user_id,
                "topic": request.topic,
                "summary": result["summary"],
                "execution_time": execution_time,
                "timestamp": datetime.now(timezone.utc),
            }
        )

        return {
            "summary": result["summary"],
            "execution_time": execution_time,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Workflow failed: {str(error)}",
        )