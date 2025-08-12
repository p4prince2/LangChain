from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Get token
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not api_key:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is missing. Check your .env file.")


# Create endpoint with token
llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

chat_model=ChatHuggingFace(llm=llm)

result=chat_model.invoke("which language we must have to study")

print(result.content)