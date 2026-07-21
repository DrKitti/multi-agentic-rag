import sys

from data_retriever_agent import run_data_retriever
from report_generator_agent import generate_report


def run_workflow(query: str) -> str:
    snippets = run_data_retriever(query)
    return generate_report(query, snippets)


if __name__ == "__main__":
    user_query = " ".join(sys.argv[1:]) or input("Enter your query: ")
    print(run_workflow(user_query))
