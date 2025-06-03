from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os 

# Static Prompt

# call the llm
load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="deepseek-ai/DeepSeek-R1",
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token = os.getenv("HF_API_TOKEN"),
    provider="together"
)

model = ChatHuggingFace(llm=llm)

# here this messages acts as a History
messages = [
    SystemMessage(content = "hello you are an smart ai assistant that solves all the human queries"),
    HumanMessage(content = 'tell me about the sea foods'),
]



result = model.invoke(messages)

print(result.content)

messages.append(AIMessage(result.content))

print(messages)