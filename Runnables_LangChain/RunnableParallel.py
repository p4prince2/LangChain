from langchain_huggingface import  ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from  langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)


prompt=PromptTemplate(
    template="write a tweet on the about {topic} ",
    input_variables=["topic"]
)


prompt1=PromptTemplate(
    template="write the linkedin post on about {topic}",
    input_variables=["topic"]
)

parser=StrOutputParser()

parall=RunnableParallel(
    {
        "tweet":RunnableSequence(prompt,model,parser),
        "linkedin":RunnableSequence(prompt1,model,parser)
    }

)

# we can do like these also
# parall=RunnableParallel(
#     {
#         "tweet":prompt |model |parser,
#         "linkedin":prompt1 | model | parser
#     }
# )


result=parall.invoke({"topic":"Ai"})
print(result["tweet"])
print(result["linkedin"])
