from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY")
)

system_prompt = """
You are an expert AI assistant who is capable to resolve any given complex task and then based on your thinking you can respond to user queries

for the given user query input breakdown the problem into few steps and then resolve the query and respond
atleast think 5 to 6 steps on how to solve the given problem 

you should follow this dequence 
1. user input
2. you analyse 
3. you think
4. you again think for several time 
5. when you feel it is correct time to respond please generate the answer
6. validate your response

Rule: 
1. Follow the strict JSON output as per output schema 
2. analyse and perform one step at a time 
3. carefully analyse the user query

Output format:
{{step: "String", content: "string"}}


follow these stpes in sequence - 
analyse, think, output, validation, result
as given inbelow example
Example:
Input: what is 2+2
Output: {{ step: "analyse", content: "user is asking mathematics related query"}}
Output: {{ step: "think", content: "for addition there are some rules to follow like go from left to right"}}
Output: {{ step: "output", content: "4"}}
Output: {{ step: "validation", content: "if you have 2 mangos and another 2 mangos then in total you will have 4 mangos"}}
Output: {{ step: "result", content: "2+2 = 4"}}

"""



response = client.chat.completions.create(
    model="gpt-4o",
    response_format= {"type": "json_object"},
    messages= [
        {"role": "system", "content": system_prompt },
        {"role": "user", "content":  "what is 4+8*2"},

        # this we have added after the run of first iteration
        {"role": "assistant" , "content": json.dumps({ "step": "analyse", "content": "user is asking a mathematics-related query involving both addition and multiplication."}
)}

    ]
)

print(f"The response is: {response.choices[0].message.content}")