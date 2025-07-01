from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chat_model = ChatOpenAI(model = "gpt-4", api_key=os.getenv("OPEN_AI_KEY"), temperature=0.4, max_completion_tokens=25)

response = chat_model.invoke("what is gravity?")

print(response) # Response consist of actual text content as well as different meta data.

print(response.content)