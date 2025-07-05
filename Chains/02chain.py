# this is a simple chain 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser


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

parser = StrOutputParser()

chain = prompt_templae1 | model | parser | prompt_templae2 | model | parser

topic = input('> ')
result = chain.invoke({"topic": topic})
print(result)