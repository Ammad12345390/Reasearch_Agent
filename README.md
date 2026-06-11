# Research Agent API

## Overview

Research Agent API is a FastAPI-based application that uses a simple Agentic AI workflow to generate research summaries on a given topic. The system consists of two agents:

1. **Researcher Agent** – Collects and generates key facts about a topic.
2. **Summarizer Agent** – Creates a concise summary from the generated facts.

The application is built using FastAPI, LangGraph, Pydantic, and MongoDB, providing a scalable foundation for AI-powered research automation.

---

## Features

* FastAPI asynchronous API
* LangGraph-based agent workflow
* Researcher and Summarizer agents
* Pydantic request and response validation
* MongoDB logging
* Execution time tracking
* RESTful API architecture
* Clean and modular project structure

---

## Architecture

```text
Client Request
      |
      v
+----------------+
|   FastAPI API  |
+----------------+
      |
      v
+----------------+
| LangGraph Flow |
+----------------+
      |
      v
+------------------+
| Researcher Agent |
+------------------+
      |
      v
+------------------+
| Summarizer Agent |
+------------------+
      |
      v
+----------------+
| MongoDB Logger |
+----------------+
      |
      v
Client Response
```

---

## Technology Stack

### Backend

* FastAPI
* Python 3.11+
* Uvicorn

### AI Framework

* LangGraph

### Database

* MongoDB
* Motor (Async MongoDB Driver)

### Validation

* Pydantic

---

## Project Structure

```text
research_agent/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── logger.py
│   ├── schemas.py
│
├── .env
├── requirements.txt
├── README.md
│
└── venv/
```

---

## API Endpoint

### Generate Research Summary

**Endpoint**

```http
POST /research
```

### Request Body

```json
{
  "topic": "Artificial Intelligence",
  "user_id": "user123"
}
```

### Response

```json
{
  "summary": "Artificial Intelligence is a rapidly growing field that impacts multiple industries and drives innovation.",
  "execution_time": 2.01
}
```

---

## Agent Workflow

### Researcher Agent

Responsibilities:

* Receives topic
* Generates key facts
* Performs topic analysis

Example Output:

```text
Artificial Intelligence is transforming healthcare.
AI improves business decision making.
AI is widely used in automation.
```

### Summarizer Agent

Responsibilities:

* Receives facts
* Generates concise summary
* Produces final response

Example Output:

```text
Artificial Intelligence is a rapidly growing technology that improves efficiency, drives innovation, and creates opportunities across industries.
```

---

## Database Logging

Every request is logged into MongoDB.

### Logged Fields

```json
{
  "topic": "Artificial Intelligence",
  "user_id": "user123",
  "summary": "...",
  "execution_time": 2.01,
  "timestamp": "2026-06-11T12:00:00"
}
```

---

## Environment Variables

Create a `.env` file:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=research_agent
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Ammad12345390/Reasearch_Agent.git
cd Reasearch_Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the server:

```bash
uvicorn app.main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## Example API Request

Using cURL:

```bash
curl -X POST "http://127.0.0.1:8000/research" \
-H "Content-Type: application/json" \
-d '{
    "topic":"Artificial Intelligence",
    "user_id":"user123"
}'
```

---

## Future Improvements

* OpenAI Integration
* Gemini Integration
* Real Web Search
* Multi-Agent Collaboration
* Research Source Citations
* User Authentication
* Agent Memory
* Report Generation
* Vector Database Support
* RAG-based Research

---

## Learning Outcomes

This project demonstrates:

* FastAPI Development
* Agentic AI Concepts
* LangGraph Workflows
* Asynchronous Programming
* MongoDB Integration
* API Design
* Pydantic Validation
* Backend Development Best Practices

---

## Author

**Ammad Kabir**

AI Engineer | FastAPI Developer | Agentic AI Enthusiast

GitHub:
https://github.com/Ammad12345390
