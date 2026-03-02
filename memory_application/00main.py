from mem0 import Memory
from google import genai
from openai import OpenAI
# GEMINI_API_KEY= "test"
QUADRANT_HOST = "localhost"
NEO4J_URL = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO5J_PASSWORD = "reform-william-center-vibrate-press-5829"
OPENAI_API_KEY = "test"
# the above all are dummy values
# Initialize Gemini client
# client = genai.Client(api_key=GEMINI_API_KEY)

config = {
    "version": "v1.1",
    "embedder":{
        "provider": "openai",
        "config": {"api_key":OPENAI_API_KEY, "model":"text-embeding-3-small"}
    },
    "llm": {
        "provider": "openai",
        "config": {"api_key" : OPENAI_API_KEY, "model":"gpt-4.1"}
    },
    "vector_store":{
        "provider":"qdrant",
        "config":{
            "host": QUADRANT_HOST,
            "port": 6333,
        }
    },
    "graph_store":{
        "provider": "neo4j",
        "config":{"url": NEO4J_URL, "username": NEO4J_USERNAME, "password":NEO5J_PASSWORD}
    }
}


mem_client = Memory.from_config(config)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def chat(text):
    messages = [
        {"role":"user", "content": text}
    ]

    result = openai_client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )

    messages.append(
        {"role":"assistant", "content": result.choices[0].message.content}
    )

    
    return result.choices[0].message.content


# this chat is without any memory 
while(True):
    text = input("User > ")
    bot = chat(text)
    print("Bot > ", bot)


# notes:
# this is the basic question and answering with LLM without using the memory concept