from langchain_huggingface import  ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import  load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace()

prompt=PromptTemplate(
    template="write a joke about{topic}",
    input_variables=["topic"]
)

prompt1=PromptTemplate(
    template="Explain the joke {text}",
    input_variables=["text"]
)

parser=StrOutputParser()

chain=RunnableSequence(prompt ,model,parser,prompt1,model,parser)

result=chain.invoke({"topic":"Ai"})
print(result)
