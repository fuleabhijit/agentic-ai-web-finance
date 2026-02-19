from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    query: str = Field(..., min_length=5, description="Question for the AI finance/web analysis team")


class AnalyzeResponse(BaseModel):
    query: str
    answer: str
