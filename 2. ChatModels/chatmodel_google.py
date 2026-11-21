from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

google_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=google_api_key)

def get_google_response(prompt):
    response = google_model.invoke(prompt)
    return response.content