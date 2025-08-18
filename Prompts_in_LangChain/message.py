from langchain.chains.question_answering.map_reduce_prompt import messages
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import  load_dotenv



load_dotenv()

llm=HuggingFaceEndpoint(
repo_id="mistralai/Mistral-7B-Instruct-v0.2",
task="text-generation"

)

model=ChatHuggingFace(llm=llm)


messages=[
        SystemMessage(content="You are a helpful assiastant  "),
        HumanMessage(content="tell about  langchain")
          ]

result=model.invoke(messages)
messages.append(AIMessage(result.content))
print(messages)
