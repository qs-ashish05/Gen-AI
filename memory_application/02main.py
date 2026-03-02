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


# client = genai.Client(api_key=GEMINI_API_KEY)

config = {
    "version": "v1.1",
    "embedder":{
        "provider": "openai",
        "config": {"api_key":OPENAI_API_KEY, "model":"text-embedding-3-small"}
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
    mem_result = mem_client.search(query=text, user_id = "qs123")
    print("<Memory> : ", mem_result)
    # print("<Memory> : ", mem_result.get("result"))

    # memories = ""
    # for mem in mem_result:
    #     # res = mem.memory
    #     # score = mem.score
    #     res = mem.get("memory")
    #     score = mem.get("score")
    #     memories += f"{str(res)}: {str(score)}"

    memories = "\n".join(
    [f"{m['memory']} (score: {m['score']})"
     for m in mem_result.get("results", [])]
    )

    SYSTEN_PROMPT = f"""
        You are a memory awaire system use your memory for the ansering the user queries
        {memories}
    """

    print("The Actual memory is > \n", memories)

    messages = [
        {"role":"system", "content":SYSTEN_PROMPT},
        {"role":"user", "content": text}
    ]

    
    # retrive the knowldege from graph database
   
    result = openai_client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )

    messages.append(
        {"role":"assistant", "content": result.choices[0].message.content}
    )

    mem_client.add(messages, user_id = "qs123")
    print("added to memory")
    return result.choices[0].message.content



while(True):
    text = input("User > ")
    bot = chat(text)
    print("Bot > ", bot)

# if you wants to return the proper messags then just uncomment the codes and do a proper LLM call


# # notes:
# this is the basic question and answering with LLM using the memory concept and retrival

# MATCH p = ()-[]->() return p

# mem0 is open source project read more about that here - https://github.com/mem0ai/mem0


