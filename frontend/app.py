import os

import requests
import streamlit as st


API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Agentic AI Finance Analyzer", page_icon="📈", layout="wide")
st.title("📈 Agentic AI Web + Financial Analysis")
st.caption("Streamlit frontend powered by a FastAPI + Pydantic backend")

query = st.text_area(
    "Ask your question",
    placeholder="Compare Apple and Microsoft in terms of stock fundamentals and public sentiment from the last month",
    height=120,
)

if st.button("Analyze", type="primary"):
    if not query.strip():
        st.warning("Please enter a question before running analysis.")
    else:
        with st.spinner("Running multi-agent analysis..."):
            try:
                response = requests.post(
                    f"{API_BASE_URL}/analyze",
                    json={"query": query.strip()},
                    timeout=120,
                )
                if response.status_code == 200:
                    st.markdown(response.json().get("answer", "No response content."))
                else:
                    st.error(f"API error ({response.status_code}): {response.text}")
            except requests.RequestException as exc:
                st.error(f"Request failed: {exc}")

st.divider()
st.write("Backend:", API_BASE_URL)
