from langchain_huggingface import  ChatHuggingFace,HuggingFaceEndpoint
from dotenv import  load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from sqlalchemy.orm import merge_result

from Sequentical_chain import prompt1

load_dotenv()

llm=HuggingFaceEndpoint(
repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"]
)

prompt2=PromptTemplate(
template="Generate 5 short question from the following  text \n {text}",
    input_variables=["text"]
)

prompt3=PromptTemplate(
template="Merge the provided notes and quiz  into a single document \n notes ->{notes} and quiz ->{quiz}",
    input_variables=["notes","quiz"]
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    "notes":prompt1 | model | parser,
    "quiz":prompt2 | model | parser

})


merge_chain=prompt3 | model | parser

chain= parallel_chain | merge_chain

text="""
 something you need to perform the operation

"""

result=chain.invoke({"text": "___.txt"})

print(result)


## chain.get_graph().print_ascii()    ## for visual