from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


chat_templet=ChatPromptTemplate([
    ("system","you are a helpful customer support agent"),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human","{query}")
])

chat_history=[]

with open("chat_history.txt") as f:
    chat_history.extend(f.readline())
print(chat_history)


chat_templet.invoke({"c hat_history":chat_history,
'query': "where i my refund"})