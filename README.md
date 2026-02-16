# 🤖 Agentic AI Web + Finance Analyzer (FastAPI + Streamlit + Pydantic)

This project is now structured as a **Python web app** with:
- **FastAPI** backend (API endpoints)
- **Pydantic** schemas (request/response validation)
- **Streamlit** frontend (simple UI)
- **Agno multi-agent team** for web research + financial analysis

## 📁 Project Structure

```text
backend/
  main.py              # FastAPI app + endpoints
  schemas.py           # Pydantic models
  services/agents.py   # Agno agents + execution
frontend/
  app.py               # Streamlit UI
requirements.txt
```

## ⚙️ Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add environment variables (`.env`):

```env
GROQ_API_KEY=your_groq_api_key_here
```

## ▶️ Run the app

### 1) Start FastAPI backend

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

API docs: `http://localhost:8000/docs`

### 2) Start Streamlit frontend

```bash
streamlit run frontend/app.py
```

By default, frontend calls `http://localhost:8000`.

To change backend URL:

```bash
API_BASE_URL=http://localhost:8000 streamlit run frontend/app.py
```

## 🧪 Example API Request

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"query":"Compare Apple and Microsoft in terms of stock fundamentals and public sentiment from the last month"}'
```

## Notes

- If `GROQ_API_KEY` is missing, `/analyze` will return an error.
- The response is markdown-ready and rendered directly in Streamlit.
