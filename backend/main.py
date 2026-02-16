from fastapi import FastAPI, HTTPException

from backend.schemas import AnalyzeRequest, AnalyzeResponse
from backend.services.agents import run_analysis


app = FastAPI(
    title="Agentic AI Web + Finance API",
    description="FastAPI backend for multi-agent web and finance analysis",
    version="1.0.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest) -> AnalyzeResponse:
    try:
        answer = run_analysis(payload.query)
        return AnalyzeResponse(query=payload.query, answer=answer)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {exc}") from exc
