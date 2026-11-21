from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

anthropic_model = ChatAnthropic(model="claude-3-5-sonnet-20261026", api_key=anthropic_api_key)

def get_anthropic_response(prompt):
    response = anthropic_model.invoke(prompt)
    return response.content

