import re
import sys
from pathlib import Path


KNOWLEDGE_BASE_PATH = Path(__file__).resolve().parents[1] / "knowledge_base.txt"
STOPWORDS = {"a", "an", "and", "for", "in", "is", "of", "on", "the", "to", "what", "which", "with"}


def load_knowledge_base() -> str:
    return KNOWLEDGE_BASE_PATH.read_text(encoding="utf-8")


def split_into_chunks(text: str) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    chunks = []

    for paragraph in paragraphs:
        previous_is_heading = chunks and "\n" not in chunks[-1] and len(chunks[-1]) < 80

        if previous_is_heading:
            chunks[-1] += f"\n\n{paragraph}"
        else:
            chunks.append(paragraph)

    return chunks


def tokenize(text: str) -> set[str]:
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())
    return {word for word in words if word not in STOPWORDS}


def keyword_search(query: str, chunks: list[str], top_k: int = 3) -> list[str]:
    query_words = tokenize(query)
    scored_chunks = [
        (len(query_words & tokenize(chunk)), chunk)
        for chunk in chunks
    ]
    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:top_k] if score > 0]


def retrieve(query: str, top_k: int = 3) -> list[str]:
    text = load_knowledge_base()
    chunks = split_into_chunks(text)
    return keyword_search(query, chunks, top_k)


if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) or input("Enter your query: ")

    for index, snippet in enumerate(retrieve(query), start=1):
        print(f"\n[{index}]\n{snippet}")
