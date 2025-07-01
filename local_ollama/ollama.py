from fastapi import FastAPI
from ollama import Client

app = FastAPI()

client = Client(
    host = 'http/127.0.0.1:11434'
)


client.pull('gemma3:1b')
@app.get("/chat")
def get_response():
    response = client.chat(model = 'gemma3:1b', messages=[
        {'role': 'user', 'content': 'hey there'}

    ])

    return response['message']['content']
