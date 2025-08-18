from langchain_core.prompts import ChatPromptTemplate

chat_templet=ChatPromptTemplate(
    [
        ("system","you are a helpful {domain} expert"),
        ("huma","Explain in simple terms, what is  {topic} ")

    ]

)

promt=chat_templet.invoke({'domain':"cricket","topic":"no ball"})

print(promt)
