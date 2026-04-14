from langchain_community.tools import DuckDuckGoSearchResults
from dotenv import load_dotenv

load_dotenv()

def tools_search():
    search = DuckDuckGoSearchResults()
    results = search.invoke("What is the capital of Pakistan?")
    return results

tools_search()