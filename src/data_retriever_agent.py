import sys

from langchain.agents import create_agent
from langchain_core.messages import ToolMessage
from langchain.tools import tool

from llm import create_llm
from retriever import NO_RESULTS_MESSAGE, retrieve


SYSTEM_PROMPT = """You are a Data Retriever Agent.
Call the retrieve_knowledge tool exactly once to search the knowledge base.
Do not answer, summarize, or rewrite the user's question.
"""


@tool
def retrieve_knowledge(query: str) -> str:
    """Search the local knowledge base and return relevant raw snippets."""
    snippets = retrieve(query)
    return "\n\n---\n\n".join(snippets) or NO_RESULTS_MESSAGE


def create_data_retriever_agent():
    return create_agent(
        model=create_llm(),
        tools=[retrieve_knowledge],
        system_prompt=SYSTEM_PROMPT,
        name="data_retriever_agent",
        interrupt_after=["tools"],
    )


def run_data_retriever(query: str) -> str:
    agent = create_data_retriever_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": query}]})

    for message in reversed(result["messages"]):
        if isinstance(message, ToolMessage):
            return message.content

    raise RuntimeError("Data Retriever Agent did not call the retrieval tool.")


if __name__ == "__main__":
    user_query = " ".join(sys.argv[1:]) or input("Enter your query: ")
    print(run_data_retriever(user_query))
