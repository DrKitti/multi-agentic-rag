# BBL Innovation Data and AI Fest 2026 Test : Multi Agentic RAG

<div class="display: flex; justify-content: center;">
  <img height="100" alt="image" src="" />
</div>



by Kittithuch Somarkphan

## Project Overview

This project is a sequential Multi-Agent Retrieval-Augmented Generation (RAG) system built with LangChain using gpt5-mini as the LLM for the agents.

The system consists of two agents:
- Data Retriever Agent : Searches the knowledge base and retrieves relevant information.
- Report Generator Agent : Combines the retrieved information into a clear and easy-to-understand answer.


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
