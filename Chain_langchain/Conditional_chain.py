from re import template

from dotenv.variables import Literal
from langchain_huggingface import  ChatHuggingFace, HuggingFaceEndpoint
from dotenv import  load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from  langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import  BaseModel,Field

from Simple_chain import result

load_dotenv()

llm=HuggingFaceEndpoint(
repo_id="google/gemma-2-2b-it",
    task="text-generation"

)

model=ChatHuggingFace(llm=llm)

class Feedback(BaseModel):

    sentiment : Literal["positive",'negative'] = Field(description="give the sentiment of the feedback")

parser=StrOutputParser()
Pydantic_parser1=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":Pydantic_parser1.get_format_instructions()}
)

prompt2=PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

classifier_chain=prompt1 | model | Pydantic_parser1

branch_chain=RunnableBranch(
    (lambda x:x["sentiment"]=="positive" ,prompt2 | model | parser),
    (lambda x:x["sentiment"]=="negative" ,prompt3 | model | parser),
  RunnableLambda(lambda x:"Could not find sentiment")
)


chain= classifier_chain | branch_chain

result=chain.invoke({"feedback":"i love my country"})

print(result)