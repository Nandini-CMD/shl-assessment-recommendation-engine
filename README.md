# 🧠 SHL Assessment Recommendation Engine  
### GenAI-Inspired Semantic Recommendation System

This project implements a **content-based assessment recommendation system** designed to help recruiters and hiring teams select the most suitable **SHL assessments** using **natural language job descriptions**.

By leveraging **SentenceTransformer embeddings**, **FAISS for fast semantic similarity search**, and a **RAG-inspired retrieval architecture**, the system recommends relevant assessments along with **clear, explainable reasoning**.  
The application is presented through a lightweight **HTML + JavaScript frontend** backed by a **Flask REST API**.

⚠️ **Note:**  
The project is intentionally designed for **local execution only** to ensure reliability during automated evaluation and to avoid broken or inaccessible deployment links.

---

## 🌟 Key Features

- 🔍 Semantic (meaning-based) assessment recommendations  
- 🧠 Natural language input for job requirements  
- ⚙️ SentenceTransformer embeddings (no paid APIs)  
- ⚡ Fast similarity search using **FAISS**  
- 📊 Explainable, deterministic recommendations  
- 💻 Clean web interface with Flask backend  
- 🧪 Fully local & reproducible (evaluation-safe)

---

## 🎯 Problem Statement

Recruiters often face difficulty selecting the correct SHL assessment from a large catalog based on:
- Skills required  
- Job role context  
- Test duration  
- Cognitive vs behavioral focus  

Traditional keyword matching systems fail to capture intent and context.

### Goal
Build a system that:
- Accepts job requirements in **natural language**
- Understands **semantic meaning**, not just keywords
- Recommends the **most relevant SHL assessments**
- Provides **transparent explanations** for each recommendation

---

## 🧠 Model Architecture and Purpose

### 📝 Sentence Embeddings (Semantic Representation)

- **Model**: `all-MiniLM-L6-v2` (SentenceTransformers)
- **Embedding Size**: 384-dimensional vectors
- **Purpose**: Convert text into dense vectors capturing semantic meaning

Each SHL assessment is represented as a **single rich document** combining:
- Assessment name  
- Skills tested  
- Duration  
- Test type  
- Description  

This improves contextual understanding and retrieval quality.

#### Why SentenceTransformers?
- Captures semantic similarity beyond keywords
- Lightweight and fast
- Pretrained using contrastive learning
- Fully open-source (no API keys, no cost)

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
```

## 🏗️ System Architecture (Detailed Explanation)

The SHL Assessment Recommendation Engine follows a **modular, retrieval-first architecture** inspired by modern GenAI systems used in HR tech and search platforms.

---

### 🔹 High-Level Architecture Flow
```python
User (Browser)
        ↓
Frontend (HTML + JavaScript)
        ↓
Flask REST API (/recommend)
        ↓
SentenceTransformer Embeddings
        ↓
FAISS Vector Index
        ↓
Top-K Relevant Assessments
        ↓
Explanation Generator
        ↓
Results Displayed to User
```
## 🗂️ Project Structure
```pyhton
shl-assessment-recommendation-engine/
│
├── backend/
│   ├── app.py              # Flask API
│   └── rag_engine.py       # Embeddings + FAISS logic
│
├── frontend/
│   └── index.html          # Web UI
│
├── data/
│   └── SHL_catalog.csv     # SHL assessment dataset
│
├── requirements.txt
├── README.md
└── .gitignore
```
## 🛠️ Installation & Setup

### 🔧 Prerequisites
 -Python ≥ 3.8
 -pip
 -Virtual environment (recommended)

## 📦 Steps
### 1️⃣ Clone the Repository
```
git clone <your-github-repo-url>
cd shl-assessment-recommendation-engine
```

### 2️⃣ Create & Activate Virtual Environment
```python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install Dependencies
```pip install -r requirements.txt```






