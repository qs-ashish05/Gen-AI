from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

prompt_template = PromptTemplate(
    template="give me 5 facts about the {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)


chain = prompt_template | model | parser

result = chain.invoke({'topic': "gravity"})
print(result) 