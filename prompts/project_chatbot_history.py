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
chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("A.I",result.content)

print("chat History is: ",chat_history)


# problem with this approach is that 
# 1. in the list it is not very fessible to store that which element is query and which element is response
# 2. hence the better approach is we store this into a dictionary
# 3. format of dictionary is: {user: <> Ai: <>}
# 4. For the long conversation we can use nested dictionary

# # {
#     {'user': <>, "AI": <>}
#     {'user': <>, "AI": <>}
#     {'user': <>, "AI": <>}
#     {'user': <>, "AI": <>}
# }