from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  StrOutputParser
from dotenv import load_dotenv
from  langchain_core.runnables import RunnablePassthrough,RunnableParallel,RunnableSequence

from RunnaleSequence import result

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)


model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt=PromptTemplate(
    template="write a joke about{topic}",
    input_variables=["topic"]
)
prompt1=PromptTemplate(
    template="explain the  joke - {text}",
    input_variables=["topic"]
)

joke_chain=prompt|model|parser

Parallelchain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "explain":RunnableSequence(prompt1,model,parser)
    }
)


final_chain=joke_chain | Parallelchain

result=final_chain.invoke({"topic":"Ai"})

print(result)