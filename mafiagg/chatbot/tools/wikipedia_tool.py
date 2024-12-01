from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool


wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())


@tool
def get_wikipedia_information(query: str):
    """Get information about a query from wikipedia."""
    print(f"[Wikipedia] Query: {query}")
    return wikipedia.run(query)