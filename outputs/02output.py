# this is with annotations
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
from typing import TypedDict, Annotated

chat_model = ChatOpenAI(
    model = "gpt-4",
    api_key=os.getenv("OPEN_AI_KEY"),
    temperature=0.4,
    max_completion_tokens=25
)


class Review(TypedDict):
    summary: Annotated[str, "this is the summary of text provoded"]
    sentiment: Annotated[str, "this is the overall sentiment of the text given"]

structured_model = chat_model.with_structured_output(Review)

text = """The rapid advancement of artificial intelligence is transforming industries across the globe. From healthcare to finance, AI-powered tools are improving efficiency, enhancing decision-making, and enabling new capabilities. However, this progress also raises important ethical concerns, such as data privacy, algorithmic bias, and job displacement. As technology continues to evolve, it is essential for policymakers, developers, and society to work together to ensure AI is used responsibly and for the benefit of all."""

response = structured_model.invoke(text)

print(f"The response is \n {response}")
print(f"The summary is \n {response['summary']}")
print(f"The sentiment is \n {response['sentiment']}")
