from langchain.agents import create_agent

from llm import create_llm
from retriever import NO_RESULTS_MESSAGE


SYSTEM_PROMPT = """You are a Report Generator Agent.
Answer the user's question using only the retrieved snippets provided to you.
Create a clear, cohesive, non-redundant, and well-formatted answer.
Respond in the same language as the user's question.
If no relevant information was found, clearly tell the user that the knowledge base
does not contain the requested information. Do not answer from your own knowledge.
"""


def create_report_generator_agent():
    return create_agent(
        model=create_llm(),
        tools=[],
        system_prompt=SYSTEM_PROMPT,
        name="report_generator_agent",
    )


def generate_report(query: str, snippets: str) -> str:
    context = snippets.strip() or NO_RESULTS_MESSAGE
    prompt = f"""User question:
{query}

Retrieved snippets:
{context}

Write the final answer."""

    agent = create_report_generator_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
    return result["messages"][-1].content
