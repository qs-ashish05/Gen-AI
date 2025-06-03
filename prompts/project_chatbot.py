from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token = os.getenv("HF_API_TOKEN"),
    provider="together",
    temperature=0.6,
    max_new_tokens=10
)

model = ChatHuggingFace(llm = llm)

while True:
    user_input = input("You: ")
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print("A.I",result.content)


# this chatbot will not have an chat history