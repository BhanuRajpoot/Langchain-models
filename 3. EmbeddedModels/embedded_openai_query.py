from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=openai_api_key, dimensions=32)

print(embeddings.embed_query("Hello, how are you?"))