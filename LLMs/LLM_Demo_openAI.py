from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(model = "gpt-3.5-turbo-instruct", api_key=os.getenv("OPEN_AI_KEY"))

while(True):
    query = input("> ")
    response = llm.invoke(query)
    print(response)  

# The llm model response is only text as per the definition that it takes text as input and
# gives text as output 