# AI Career Coach 🚀

An AI-powered career coaching application that helps users understand their professional profiles through resume analysis and intelligent question answering.

Built using **Python, Flask, LangChain, Ollama, Hugging Face Embeddings, and FAISS**, the application combines Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) to provide contextual insights from uploaded resumes.

## 🎯 Project Overview

The AI Career Coach is designed to simplify resume analysis and help individuals better understand their professional qualifications.

Users can upload PDF resumes, receive AI-generated summaries, and ask questions about their uploaded documents using a RAG-powered question-answering system.

## ✨ Key Features

- **Resume Analysis:** Uses an LLM to generate structured resume summaries.
- **PDF Processing:** Extracts text from uploaded PDF documents.
- **Text Chunking:** Splits extracted documents into manageable chunks using Recursive Character Text Splitter.
- **Semantic Embeddings:** Uses Hugging Face embeddings to transform text into numerical representations.
- **Vector Search:** Stores and retrieves relevant document information using FAISS.
- **RAG Question Answering:** Retrieves relevant resume information to provide contextual answers.
- **Web Interface:** Uses Flask to provide a simple interface for interacting with the application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| LangChain | LLM application development |
| Ollama | Local LLM inference |
| Qwen 2.5 (3B) | Language model |
| Hugging Face | Text embeddings |
| FAISS | Vector database and similarity search |
| PyPDF2 | PDF text extraction |

## ⚙️ Application Workflow

1. User uploads a resume in PDF format.
2. PyPDF2 extracts the document text.
3. RecursiveCharacterTextSplitter divides the text into chunks.
4. Hugging Face Embeddings converts the chunks into vector representations.
5. FAISS stores the vectors for similarity search.
6. Ollama runs the Qwen 2.5 model to generate a structured resume summary.
7. Users submit questions about their resumes.
8. The RAG pipeline retrieves relevant information and generates contextual responses.

## 🏗️ Project Architecture

```text
AI Career Coach
      |
      v
Flask Web Application
      |
      v
Resume Upload (PDF)
      |
      v
PDF Text Extraction
      |
      v
Text Splitting
      |
      v
Hugging Face Embeddings
      |
      v
FAISS Vector Database
      |
      v
Similarity Search
      |
      v
Ollama (Qwen 2.5 3B)
      |
      v
AI-Generated Resume Insights
      |
      v
Question Answering (RAG)
```

## 📂 Project Structure

```text
Ai-career-coach/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── results.html
│   ├── ask.html
│   └── qa_results.html
│
├── uploads/
├── vector_index/
├── .venv/
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vedline2547/AI-career-coach.git
cd Ai-career-coach
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask langchain langchain-classic langchain-community langchain-ollama langchain-huggingface langchain-text-splitters faiss-cpu sentence-transformers PyPDF2
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/

Pull the language model:

```bash
ollama pull qwen2.5:3b
```

Ensure Ollama is running before launching the application.

### 5. Run the application

```bash
python main.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 🧠 Core AI Concepts Demonstrated

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Text embeddings
- Semantic similarity search
- Vector databases
- Document processing
- Prompt engineering
- LLM application development
- Flask-based AI deployment

## 🔮 Future Improvements

- Conversation memory for multi-turn interactions.
- Job description and resume matching.
- Skills gap analysis.
- Career path recommendations.
- Resume improvement suggestions.
- Support for additional document formats.

## 👨‍💻 Author

**Vedline Ochieng**

Civil Engineering Student | Machine Learning Enthusiast | Python Developer | AI Engineer in Progress

GitHub: [@Vedline2547](https://github.com/Vedline2547)

---

*Building AI-powered solutions through practical machine learning and software engineering.*
