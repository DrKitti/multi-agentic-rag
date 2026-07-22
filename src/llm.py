import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def create_llm() -> ChatOpenAI:
    load_dotenv()
    api_key = os.getenv("AZURE_OPENAI_API_KEY")

    if not api_key:
        raise ValueError("AZURE_OPENAI_API_KEY is missing. Add it to the .env file.")

    endpoint = os.getenv(
        "AZURE_OPENAI_ENDPOINT",
        "https://oaibblinnocandiddate01.openai.azure.com/",
    )

    return ChatOpenAI(
        api_key=api_key,
        base_url=f"{endpoint.rstrip('/')}/openai/v1/",
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5-mini"),
        max_completion_tokens=2048,
        use_responses_api=False,
    )
