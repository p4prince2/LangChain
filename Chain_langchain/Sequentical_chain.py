from langchain_huggingface import  HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from Simple_chain import prompt, result

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

prompt1=PromptTemplate(
    template="Generate a detail report on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Generate 5 funny facts from the text \n {text}",
    input_variables=["text"]
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()


chain=prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({"topic":"Love"})

print(result)