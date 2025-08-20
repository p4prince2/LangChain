from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import  load_dotenv
from  langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from stroutputparser import result

load_dotenv()

llm=HuggingFaceEndpoint(

    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

templet1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']

)

templet2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']

)

parser=StrOutputParser()


chain= templet1 | model | parser | templet2 |  model | parser

result=chain.invoke({"topic":"Black Hole"})

print(result)