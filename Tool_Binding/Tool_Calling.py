from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
import os

# 1. Setup OpenRouter API
os.environ["OPENAI_API_KEY"] = "Your key"
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

# 2. Define a tool /tool create
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b


# 3. Load LLM from OpenRouter
llm = ChatOpenAI(model="openai/gpt-4o-mini", temperature=0)

# 4. Bind tool
llm_with_tools = llm.bind_tools([multiply])

# 5. Call the model Tool Execution

  # tool calling
query=HumanMessage("What is 12 * 9?")
message=[query]
response = llm_with_tools.invoke(message)
message.append(response)


 # tool Execution
tool_mess=multiply.invoke(response.tool_calls[0])
message.append(tool_mess)

result=llm_with_tools.invoke(message).content
print(result)