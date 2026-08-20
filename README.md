# AutoStream AI Agent

A GenAI-powered conversational agent for AutoStream, a fictional SaaS platform for automated video editing.

The agent can understand user intent, answer product-related questions using a knowledge base, and capture high-intent leads through a multi-turn conversation workflow.

## Features

- LLM-based intent detection
- LLaMA 3.1 8B Instant through Groq
- Context-augmented product knowledge retrieval
- Multi-turn lead qualification
- Email validation
- Lead capture tool workflow
- Streamlit chat interface
- CLI interface for local testing
- Environment-based API key management
- Basic error handling

## Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Agent
 │
 ├── Intent Detection ──► Groq / LLaMA 3.1
 │
 ├── Product Questions ──► Knowledge Base ──► Groq / LLaMA 3.1
 │
 └── High Intent
       │
       ▼
   Lead Collection
   Name → Email → Platform
       │
       ▼
   Lead Capture Tool