# 🤖 Agentic AI Web + Finance Analyzer (FastAPI + Streamlit + Pydantic)

A Python app for AI-powered web research and financial market analysis.
FastAPI provides backend APIs and Pydantic validates request/response data.
Streamlit offers a simple UI to submit prompts and view markdown results.
Agno multi-agents combine web insights and finance tools into one response.

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

## 🚀 Deploy (easy way)

Deploy backend and frontend as **two services**.

### A) Deploy FastAPI backend (Render/Railway/Fly.io)

- **Start command**:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

- **Environment variables**:
  - `GROQ_API_KEY=...`

After deploy, copy backend URL (example: `https://my-api.onrender.com`).

### B) Deploy Streamlit frontend (Streamlit Community Cloud)

- Set **main file path** to:

```text
frontend/app.py
```

- Add **environment variables / secrets**:
  - `API_BASE_URL=https://my-api.onrender.com`

- Deploy, then open your Streamlit URL.

### C) One-machine deployment (VM / Docker host)

Run backend and frontend as separate processes:

```bash
# backend
uvicorn backend.main:app --host 0.0.0.0 --port 8000

# frontend
API_BASE_URL=http://<server-ip>:8000 streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0
```

Expose ports:
- `8000` for FastAPI
- `8501` for Streamlit

## 🧪 Example API Request

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"query":"Compare Apple and Microsoft in terms of stock fundamentals and public sentiment from the last month"}'
```

## Notes

- If `GROQ_API_KEY` is missing, `/analyze` will return an error.
- The response is markdown-ready and rendered directly in Streamlit.
