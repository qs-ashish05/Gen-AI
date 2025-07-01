from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HF_API_TOKEN")
print(hf_token)
if hf_token:
    print("Inside the 'if hf_token' block, hf_token:", hf_token)
    llm = HuggingFaceEndpoint(
        repo_id="google/gemma-3-1b-it",
        task="text-generation",
        huggingfacehub_api_token=hf_token,
        max_new_tokens=150  # Increased max_new_tokens
    )
    # Initialize ChatHuggingFace directly with the HuggingFaceEndpoint instance
    model = ChatHuggingFace(llm=llm)
    try:
        result = model.invoke('Who is Lincoln')
        print(result)
    except Exception as e:
        print(f"Error during model invocation: Type: {type(e)}, Message: {e}")
else:
    print("Hugging Face model could not be initialized due to missing token.")