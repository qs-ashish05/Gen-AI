from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os 
import streamlit as st

# Static Prompt

# call the llm
load_dotenv()
def get_response(query):
    llm = HuggingFaceEndpoint(
        # repo_id="deepseek-ai/DeepSeek-R1",
        repo_id="deepseek-ai/DeepSeek-R1-0528",
        task="text-generation",
        huggingfacehub_api_token = os.getenv("HF_API_TOKEN"),
        provider="together"
    )

    model = ChatHuggingFace(llm=llm)

    result = model.invoke(query)
    return result.content


# Ui elements
st.header("Research Tool")

user_input = st.text_input("Enter Your Prompt")

if st.button("Summerize"):
    st.write(get_response(user_input))
