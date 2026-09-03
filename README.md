# 📖 Gita Updesha ChatBot — Agentic RAG with CrewAI, Ollama & PGVector

An open-source AI chatbot that answers questions from the Bhagavad Gita using Retrieval-Augmented Generation (RAG), multi-agent orchestration, and modern LLM tooling.

## Why this project?

Studying the Bhagavad Gita often requires searching through multiple chapters and commentaries. This project makes it interactive and accessible by combining:

📚 Document ingestion & chunking

🔎 Semantic retrieval with PGVector

🤖 Agentic orchestration with CrewAI & LangGraph

🧠 LLM-powered contextual answers

🌐 FastAPI backend with Streamlit UI

## Features

📖 Question answering from Bhagavad Gita verses

🧩 Document ingestion, chunking & embedding storage in PostgreSQL + PGVector

🔎 Retrieval-Augmented Generation (RAG) pipeline for contextual responses

🤖 Multi-agent orchestration with CrewAI + LangGraph

🌐 FastAPI backend with REST APIs

🎨 Streamlit front-end for interactive Q&A

📝 Citation handling with metadata

⚡ LLM integration via Ollama models

## Tech Stack

1. Python 3.10+

2. FastAPI (backend APIs)

3. Streamlit (frontend UI)

4. LangGraph + CrewAI (multi-agent orchestration)

5. LangChain (retrieval flows)

6. Ollama (LLM hosting)

7. PostgreSQL + PGVector (vector storage)

8. Docling (document processing)

9. Arize Phoenix (prompt lifecycle management & observability)

## Project Structure

.
├── streamLit_app.py       # Streamlit front-end
├── docker-compose.yml     # Deployment setup
├── requirements.txt       # Python dependencies
├── src/
│   ├── api.py             # FastAPI endpoints
│   ├── agents.py          # CrewAI agents
│   ├── rag.py             # RAG pipeline
│   ├── rag_engine.py      # Retrieval engine
│   ├── vector_store.py    # PGVector integration
│   ├── document_processor.py # Ingestion & chunking
│   ├── memory.py          # Conversation memory
│   ├── tools.py           # Utility functions
│   └── config.py          # Settings & environment
└── data/                  # Gita text & documents

## Prerequisites

Python 3.10 or newer

PostgreSQL with PGVector extension

Ollama installed & running locally

API keys / configs for:

Arize Phoenix

CrewAI

## Environment Variables

DATABASE_URL=postgresql://user:password@localhost:5432/gita_db
OLLAMA_MODEL=gpt4
CREWAI_TRACING_ENABLED=true
ARIZE_API_KEY=our_arize_api_key

## Installation
1. create virtual environment ===>>
python -m venv .venv
.venv\Scripts\activate   # On Windows
pip install -r requirements.txt

with conda:

conda create -n gita python=3.11 -y
conda activate gita
pip install -r requirements.txt


2. Running the App
Start the FastAPI backend:

3.  Run Backend on  bash 
uvicorn src.api:app --reload

4. Run the Streamlit frontend:

5. Run Front end on  bash
streamlit run streamLit_app.py

Open your browser at:

7. Test Code
http://127.0.0.1:8501/


## API Endpoints

GET / — Root endpoint

POST /ask — Submit a question


Example request:

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What does Krishna say about duty in Chapter 2?"}'

```

## How the Workflow Works
1. User submits a question.

2. Document processor ingests & chunks Gita text.

3. Embeddings stored in PGVector.

4. RAG pipeline retrieves relevant verses.

5. CrewAI agents orchestrate multi-step reasoning.

6. Ollama LLM generates contextual answer with citations.

7. Response returned via FastAPI & displayed in Streamlit.

## Contributing

Contributions are welcome!

1. Fork the repo

2. Create a feature branch

3. Make changes

4. Open a pull request

## Acknowledgments

⚡ This project combines Agentic AI, RAG, and LLM orchestration to make the wisdom of the Bhagavad Gita accessible in an interactive way.

