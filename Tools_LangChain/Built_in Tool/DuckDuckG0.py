from langchain_community.tools import DuckDuckGoSearchRun

# Initialize the DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

# Query
query = "recent developments between India and China"

try:
    # Perform the search
    result = search_tool.invoke(query)

    print("Search Results:\n")
    print(result)
    print("--------------------------")
    print(search_tool.name)
    print("--------------------------")
    print(search_tool.description)
    print("--------------------------")
    print(search_tool.args)
except Exception as e:
    print("Error occurred:", e)
