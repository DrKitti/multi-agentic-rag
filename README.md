# Bangkok Bank Innovation Data and AI Fest 2026 Test : Multi Agentic RAG

<div class="display: flex; justify-content: center;">
  <img width="300" height="120" alt="logo BBL_eng_blue_1" src="https://github.com/user-attachments/assets/390cb6f9-05ba-4a59-b3b0-bafa6e1f1bd8" />
</div>

## Project Overview

This project is a sequential Multi-Agent Retrieval-Augmented Generation (RAG) system built with LangChain using **gpt5-mini** as the LLM for the agents.

The system consists of two agents:
- Data Retriever Agent : Searches the knowledge base and retrieves relevant information.
- Report Generator Agent : Combines the retrieved information into a clear and easy-to-understand answer.

---

## Project Structure

```
multi-agentic-rag/
├── README.md                         # Project documentation and usage instructions
├── requirements.txt                  # Python dependencies
├── knowledge_base.txt                # Local product knowledge base
├── .env.example                      # Example environment variables
├── .gitignore                        # Files excluded from Git
└── src/
    ├── __init__.py                   # Python package initialization
    ├── main.py                       # Sequential multi-agent orchestration
    ├── llm.py                        # LLM configuration and initialization
    ├── retriever.py                  # Text chunking and keyword retrieval logic
    ├── data_retriever_agent.py       # Agent for retrieving relevant snippets
    └── report_generator_agent.py     # Agent for generating the final answer
```

---

## Workflow


---

## How to run

### 1. Clone the Repository

```bash
git clone https://github.com/DrKitti/multi-agentic-rag.git
cd multi-agentic-rag
```

### 2. Set Up Python Virtual Environment

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
Install all packages that needed for this project.

### 4. Configure environment variables

```env
TYPHOON_API_KEY=your_api_key_here
TYPHOON_BASE_URL=https://api.opentyphoon.ai/v1
TYPHOON_MODEL=typhoon-v2.5-30b-a3b-instruct
```

Setup API for LLM Calling.

### 5. Run Script

**Windows:**
```cmd
python src\main.py "Which computer is best for students?"
```

**macOS/Linux:**
```bash
python3 src/main.py "Which computer is best for students?"
```

Or you can run **retriever.py** instead of main.py for testing retrieval only.

---

## Result
