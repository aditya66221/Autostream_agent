# AutoStream AI Agent – Social-to-Lead Workflow

## Overview
This project implements a GenAI-powered conversational agent for AutoStream, a SaaS platform for automated video editing. The agent can understand user intent, answer product-related queries using RAG, and capture high-intent leads through a structured workflow.

---

## Features
- Intent Detection (LLM-based using Groq – LLaMA 3.1)
- RAG-based Knowledge Retrieval (JSON + LLM)
- Lead Capture Tool Execution
- Multi-turn Conversation Memory
- Streamlit Web UI

---

## How to Run Locally

```bash
cd autostream-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
