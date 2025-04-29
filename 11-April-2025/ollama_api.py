from fastapi import FastAPI
from ollama import Client
from fastapi import Body

app = FastAPI()
client = Client(
  host='http://localhost:11434'
)

client.pull('gemma3:1b')

@app.post("/chat")
# def chat(message: str = Body(..., description="Chat Message")):
#     response = client.chat(model="gemma3:1b", messages=[
#         { "role": "user", "content": message }
#     ])

#     return response['message']['content']


def chat():
    response = client.chat(model="gemma3:1b", messages=[
        { "role": "user", "content": "what is 2 + 2?" }
    ])

    return response['message']['content']