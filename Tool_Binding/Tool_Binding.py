from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import os

# 1. Setup OpenRouter API
os.environ["OPENAI_API_KEY"] = "Your key"
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"


# 2. Define a tool /tool create
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

# print(multiply.name)
# print(multiply.description)
# print(multiply.args)


# 3. Load LLM from OpenRouter
llm = ChatOpenAI(model="openai/gpt-4o-mini", temperature=0)

# 4. Bind tool
llm_with_tools = llm.bind_tools([multiply])


response = llm_with_tools.invoke("What is 12 * 9?")
# print(response)
print(response.tool_calls) # <- this shows structured call
