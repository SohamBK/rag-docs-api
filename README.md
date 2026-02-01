# 📄 RAG Docs API

A **production-grade Retrieval Augmented Generation (RAG) backend** built with **FastAPI**, **PostgreSQL + pgvector**, and **Gemini**.  
The system ingests documents (text & PDFs), stores vector embeddings, and answers user queries using semantic search + LLM generation.

---

## 🚀 Features

- Document ingestion with automatic chunking
- PDF & text document support
- Vector search using **pgvector**
- Semantic retrieval with **Sentence Transformers**
- Answer generation using **Gemini (OpenAI-compatible API)**
- Fully async FastAPI backend
- Dockerized setup with persistent Postgres storage
- Clean domain-driven, production-ready architecture

---

## 🏗️ Tech Stack

- **Backend:** FastAPI, Python 3.11
- **Database:** PostgreSQL 16 + pgvector
- **ORM:** SQLAlchemy (Async)
- **Embeddings:** sentence-transformers
- **LLM:** Gemini (OpenAI-compatible API)
- **Infra:** Docker, Docker Compose
- **Dependency Management:** uv

---

## 🧠 High-Level Architecture

1. Documents are uploaded and chunked
2. Chunks are embedded and stored in Postgres (pgvector)
3. Queries are embedded and matched via vector similarity
4. Top results are passed to Gemini for answer generation

---

## ▶️ Running Locally

```bash
docker compose up --build
