from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os 

load_dotenv()

print(os.getenv("HF_API_TOKEN"))

llm = HuggingFaceEndpoint(
    # repo_id="deepseek-ai/DeepSeek-R1",
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token = os.getenv("HF_API_TOKEN"),
    provider="together"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is gravity")

# print(result)
print(result.content)