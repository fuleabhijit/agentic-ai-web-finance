# 🤖 Agentic AI System for Web & Financial Analysis

This project demonstrates a **multi-agent AI system** built using Agno, where specialized agents collaborate to perform **web research** and **financial market analysis** using large language models and external tools.

The goal of this project is to understand **agent-based architectures**, tool integration, and structured AI outputs.

---

## 🎯 Project Objective

- Build and orchestrate multiple AI agents with distinct responsibilities  
- Enable real-time web search and financial data retrieval  
- Generate structured, source-backed, markdown-formatted insights  
- Learn practical agentic AI workflows using modern LLM tooling  

---

## 🧠 System Overview

The system consists of **three agents**:

### 1️⃣ Web Agent
- Searches the web for information
- Uses DuckDuckGo for real-time queries
- Returns concise, structured summaries with sources

### 2️⃣ Finance Agent
- Fetches live financial data
- Retrieves stock prices, fundamentals, and analyst recommendations
- Uses Yahoo Finance as a data source

### 3️⃣ Agent Team (Coordinator)
- Orchestrates both agents
- Combines web insights with financial analysis
- Produces a single, structured response

---

## ⚙️ Tools & Technologies

### 🧠 AI Models
- LLaMA 3.3 (70B) via Groq

### 🔧 Frameworks & Libraries
- Agno (Agent framework)
- DuckDuckGo Tools (Web Search)
- Yahoo Finance Tools (Market Data)
- Python
- dotenv

---

## 🛠️ Features

- Multi-agent collaboration
- Tool-augmented LLM responses
- Structured markdown output
- Source-backed answers
- Financial data presented in clean tables
- Concise, readable AI-generated insights

---

## ▶️ Example Queries

```python
agent_team.print_response(
  "Compare Apple and Microsoft in terms of stock fundamentals and public sentiment from the last month"
)
