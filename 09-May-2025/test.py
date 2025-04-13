from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4",
    messages= [
        {"role": "user", "content": "what is 2+2"}
    ]
)

print(response.choices[0].message.content)