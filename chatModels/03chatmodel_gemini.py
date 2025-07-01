from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3-1b-it", api_key=os.getenv("GEMINI_API_KEY"))

query = "What is gravity?"

response = model.invoke(query)

print(response.content)