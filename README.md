# Multi-Agent Customer Support AI

An intelligent multi-agent system that handles customer queries end-to-end — from intent classification and knowledge retrieval to response generation and smart escalation.

Built with **RAG + LangChain + OpenAI**.

---

### Overview

This project demonstrates a real-world AI-powered customer support architecture. Multiple specialized agents collaborate to understand user intent, retrieve accurate information from a knowledge base, generate contextual responses, and escalate complex issues when required.

---

### Key Features

- Multi-agent orchestration (Classifier → Retriever → Generator → Escalation)
- Retrieval-Augmented Generation (RAG) with ChromaDB
- Context-aware multi-turn conversations
- Advanced prompt engineering
- Production-ready FastAPI + Docker setup

---

### Tech Stack

- Python
- LangChain
- OpenAI API
- ChromaDB
- FastAPI
- Docker

---

### Architecture

1. User submits a query  
2. **Classifier Agent** detects intent  
3. **Retriever Agent** performs semantic search on the knowledge base  
4. **Generator Agent** creates a grounded response  
5. **Escalation Agent** handles unresolved or sensitive queries  

---
## Getting Started

```bash
git clone https://github.com/deepu21232729/multi-agent-customer-support.git
cd multi-agent-customer-support
pip install -r requirements.txt
