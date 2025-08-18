from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import  HumanMessage,SystemMessage,AIMessage


load_dotenv()
llm=HuggingFaceEndpoint(
repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

chat_history=[
    SystemMessage(content="You are a helpful AI assiastant")

]


while True:
    user_input=input('you:  ')
    if user_input =="exit":
        break

    chat_history.append(HumanMessage(content=user_input))
    result=model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)



print(chat_history)