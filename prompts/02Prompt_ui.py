from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
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
paper_name = st.selectbox("Select Research Paper title:", ["Select...", "Attention is all you need", "Deep minds", "Pluto the first principle"])

input_style = st.selectbox("Select the Style of explaination", ["Easy way", "Beiginer Style", "Intermediate", "Advanced", "Researcher"])

explaination_length = st.selectbox("Select the length of Explanation", ["1-2 Paragraph", "2-5 Paragraph", "5+ Paragraph"])

prompt_template = PromptTemplate(
    template="""
    Explain the research topic {paper_name} with the following specifications
    Explaination Style: {input_style}
    Explaination Length: {explaination_length}
    Include relavernt maths accordingly,
    Include relavent examples 

    If you dont know about certain Topics then response with "Insufficeient contens available" instead of gusessing and producing wrong responses,
    Ensure the summary is clear, easy and aligned with the query asked
""",
input_variables = ['paper_name', 'input_style', 'explaination_length'],
validate_template=True
)


new_promt = prompt_template.invoke(
    {
        'paper_name': paper_name,
        'input_style': input_style,
        'explaination_length': explaination_length
    }
)



if st.button("Summerize"):
    st.write(get_response(new_promt))