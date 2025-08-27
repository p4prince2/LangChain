from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnablePassthrough

from RunnablePassthrough import final_chain

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)



model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

propmt1=PromptTemplate(
    template="Write a detail report on {topic}",
    input_variables=["topic"]
)

propmt2=PromptTemplate(
    template="Summarizes the following text \n {text}",
    input_variables=["text"]
)

repo_reg_chain=propmt1 | model |parser

branch_chain=RunnableBranch(
    #(condtion,output),
    (lambda x :len(x.split())>500,RunnableSequence(propmt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(repo_reg_chain,branch_chain)

result=final_chain.invoke({"topic":"Ai"})

print(result)