from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel,Field

from jsonoutputparser import final_result
from stroutputparser import result

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id=,
    task=
)

model=ChatHuggingFace(llm=llm)

class Human(BaseModel):
    name:str=Field(description="Name of the Human")
    age:int=Field(gt=18,description="Age of the Human")
    city:str=Field(description="Name of the city the person belongs to")


parser=PydanticOutputParser(pydantic_object=Human)

templet=PromptTemplate(
    template="Generate the name ,age and the city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction":parser.get_format_instructions()}

)

prompt=templet.invoke({"place":"India"})

result=model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)