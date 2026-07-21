import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def create_llm() -> ChatOpenAI:
    load_dotenv()
    api_key = os.getenv("TYPHOON_API_KEY")

    if not api_key:
        raise ValueError("TYPHOON_API_KEY is missing. Add it to the .env file.")

    return ChatOpenAI(
        api_key=api_key,
        base_url=os.getenv("TYPHOON_BASE_URL", "https://api.opentyphoon.ai/v1"),
        model=os.getenv("TYPHOON_MODEL", "typhoon-v2.5-30b-a3b-instruct"),
        temperature=0.2,
        max_completion_tokens=512,
        use_responses_api=False,
    )
