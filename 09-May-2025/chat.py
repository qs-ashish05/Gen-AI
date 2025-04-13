from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY")
)

# to set the context
system_prompt = """
you are an AI Assistant who is specialised in mathematics.
you should not answer any query which is not related to mathematics.

for a given query help user to solve along with explanation

Example: 
Input: 2+2
Output: 2+2 is 4 which is calculated by adding 2 with 2

Input: 3*10
Output: 3*10 is 30 which is calculated by multiplying 3 with 10

Input: What color is the sky?
Output: This query is not related to maths

"""

query = input("> ")
response = client.chat.completions.create(
    model="gpt-4",
    temperature = 0.6,    # optional but good to have according to need
    max_tokens = 100,    # optional but good to have according to need
    messages= [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
)

print(response.choices[0].message.content)

# the prompting technique used is called few short prompting 

