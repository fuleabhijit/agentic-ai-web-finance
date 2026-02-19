"""Legacy entrypoint.

Use the FastAPI backend (`backend/main.py`) and Streamlit frontend (`frontend/app.py`) instead.
"""

from backend.services.agents import run_analysis


if __name__ == "__main__":
    prompt = "Compare Apple and Microsoft in terms of stock fundamentals and public sentiment from the last month"
    print(run_analysis(prompt))
