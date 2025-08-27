from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import  load_dotenv
from langchain_core.runnables import RunnableLambda,RunnableSequence,RunnableParallel,RunnablePassthrough

from RunnablePassthrough import final_chain

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)


model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

def word_counter(text):
    return len(text.split())


prompt=PromptTemplate(
    template="Write a joke on {topic}"
,
    input_variables=["topic"]
)

joke_chain=prompt | model | parser

Parallel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "words_count":RunnableLambda(lambda x:len(x.split()))
    }
)


Parallel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "words_count":RunnableLambda(word_counter)
    }
)


final_chain=joke_chain | Parallel_chain

result=final_chain.invoke({"topic":"Ai"})

print(result)