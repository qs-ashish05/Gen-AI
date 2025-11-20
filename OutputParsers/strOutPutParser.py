from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

prompt_templae1 = PromptTemplate(
    template="write  a details report on {topic}",
    input_variables=['topic']
)
prompt_templae2 = PromptTemplate(
    template="write 5 line summary on the following text  /n {text}",
    input_variables=['text']
)

prompt1 = prompt_templae1.invoke({'topic': 'politics'})

res1 = model.invoke(prompt1)

# print(res1.content)

prompt2 = prompt_templae2.invoke({"text": res1.content})

res2 = model.invoke(prompt2)

print(res2.content)