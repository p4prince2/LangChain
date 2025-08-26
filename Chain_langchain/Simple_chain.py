from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

prompt=PromptTemplate(
    template="Generate 5 funny facts about {topic}",
    input_variables=["topic"]
)

model=ChatHuggingFace(llm=llm)


parser=StrOutputParser()

chain= prompt | model | parser

result=chain.invoke({"topic":"India"})

print(result)