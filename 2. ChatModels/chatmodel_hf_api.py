from langchain_huggingface import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()

huggingface_api_key = os.getenv("HUGGINGFACEHUB_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id ="tiny_llama3-8b-8192", 
    task="text-generation",
    huggingfacehub_api_token=huggingface_api_key)

model = ChatHuggingFace(llm=llm)

def get_huggingface_response(prompt):
    response = model.invoke(prompt)
    return response.content