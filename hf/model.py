from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-1b-it",
    task="text-generation",
    # huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)

