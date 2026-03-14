from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
import google.generativeai as genai
from dotenv import load_dotenv
import os
# from langchain.chat.models import init_chat_model
from langgraph.graph import START, END, StateGraph

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash") 

class State(TypedDict):
    message: Annotated[list, add_messages]


# def chatbot(state: State):
#     messages = state.get("message")  # retrive the existing messages 
#     response = model.generate_content(messages)
#     return {"messages": [response]}


from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def chatbot(state: State):
    messages = state.get("messages", [])

    gemini_messages = []

    for m in messages:
        if isinstance(m, HumanMessage):
            gemini_messages.append({
                "role": "user",
                "parts": [m.content]
            })

        elif isinstance(m, AIMessage):
            gemini_messages.append({
                "role": "model",
                "parts": [m.content]
            })

        elif isinstance(m, SystemMessage):
            gemini_messages.append({
                "role": "user",
                "parts": [m.content]
            })

    # safety check
    if not gemini_messages:
        gemini_messages.append({
            "role": "user",
            "parts": ["Hello"]
        })

    response = model.generate_content(gemini_messages)

    return {
        "messages": [
            AIMessage(content=response.text)
        ]
    }

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()