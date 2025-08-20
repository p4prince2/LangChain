from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

from jsonoutputparser import final_result

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name="fact_1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2",description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3",description="Fact 3 about the topic"),
    ResponseSchema(name="fact_4",description="Fact 4 about the topic"),
    ResponseSchema(name="fact_5",description="Fact 5 about the topic"),
]

#parser=StructuredOutputParser(response_schemas=schema)
parser=StructuredOutputParser.from_response_schemas(schema)

templet=PromptTemplate(
    template="Give 5 fact about {topic} \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction":parser.get_format_instructions()}

)

prompt=templet.invoke({"topic":"Black Hole"})

result=model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)