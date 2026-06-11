from pydantic import BaseModel, Field


class TopicRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Topic to research and summarize"
    )

    user_id: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Unique user identifier"
    )


class TopicResponse(BaseModel):
    summary: str = Field(
        ...,
        description="Generated summary from the agent workflow"
    )

    execution_time: float = Field(
        ...,
        gt=0,
        description="Execution time in seconds"
    )