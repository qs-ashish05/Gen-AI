from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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

chat_history = [
    SystemMessage(content="You are an expert AI bot and expert in resolving the queries!"),
]

while True:
    user_input = input("You: ")
    if user_input == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(user_input)
    print("A.I",result.content)
    chat_history.append(AIMessage(content=result.content))

print(chat_history)

# this chatbot will not have an chat history