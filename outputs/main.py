from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from typing import TypedDict

load_dotenv()

chat_model = ChatOpenAI(
    model = "gpt-4",
    api_key= os.getenv("OPEN_AI_KEY"),
    temperature=0.4,
    max_completion_tokens=25
)


class Review(TypedDict):
    summary: str
    sentiment: str

# The given code may not work as the langcahin had removed the with_structured_output function now this was introduces only for the trail purpose or some 
 

structured_model = chat_model.with_structured_output(Review)

text = """The rapid advancement of artificial intelligence is transforming industries across the globe. From healthcare to finance, AI-powered tools are improving efficiency, enhancing decision-making, and enabling new capabilities. However, this progress also raises important ethical concerns, such as data privacy, algorithmic bias, and job displacement. As technology continues to evolve, it is essential for policymakers, developers, and society to work together to ensure AI is used responsibly and for the benefit of all."""

response = structured_model.invoke(text)

print(f"The response is \n {response}")
print(f"The summary is \n {response['summary']}")
print(f"The sentiment is \n {response['sentiment']}")