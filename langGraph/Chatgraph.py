from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(m.name)

model = genai.GenerativeModel("models/gemini-2.5-flash")  

class State(TypedDict):
    user_message: str
    AI_message: str
    is_codingQuestion: bool



def detect_queryType(state: State) -> State:
    # TODO: Ask Gemini whether the user's message is a coding question.

    user_message = state["user_message"]

    prompt = (
        "You are a query classifier. "
        "Reply with exactly one word — 'yes' if the following message is related "
        "to coding / programming, otherwise reply 'no'.\n\n"
        f"Message: {user_message}"
    )
    response = model.generate_content(prompt)
    answer = response.text.strip().lower()

   
    return {
        **state,
        "is_codingQuestion": answer.startswith("yes"),
    }


def respond_to_codingQuestions(state: State) -> State:
    
    user_message = state["user_message"]

    prompt = (
        "You are an helpful coding assistant. "
        "Answer the following coding question clearly and concisely. "
        "no need to include code examples.\n\n"
        f"Question: {user_message}"
    )
    response = model.generate_content(prompt)

    return {
        **state,
        "AI_message": response.text.strip(),
    }


def respond_to_generalQuestions(state: State) -> State:
    
    user_message = state["user_message"]

    prompt = (
        "You are a friendly and knowledgeable assistant. "
        "Answer the following question in a helpful, concise way.\n\n"
        f"Question: {user_message}"
    )
    response = model.generate_content(prompt)

    return {
        **state,
        "AI_message": response.text.strip(),
    }



def route_edge(state: State) -> str:
    
    if state.get("is_codingQuestion"):
        return "Respond to Coding Questions"
    return "Respond to General Questions"
# Build Graph
graph_builder = StateGraph(State)

graph_builder.add_node("Detect Query Type",          detect_queryType)
graph_builder.add_node("Respond to Coding Questions", respond_to_codingQuestions)
graph_builder.add_node("Respond to General Questions", respond_to_generalQuestions)


graph_builder.add_edge(START, "Detect Query Type")


graph_builder.add_conditional_edges("Detect Query Type", route_edge)

graph_builder.add_edge("Respond to Coding Questions",  END)
graph_builder.add_edge("Respond to General Questions", END)

my_graph = graph_builder.compile()



def call_graph(user_message: str) -> str:
    initial_state: State = {
        "user_message": user_message,
        "AI_message": "",
        "is_codingQuestion": False,
    }
    result = my_graph.invoke(initial_state)
    return result["AI_message"]


def main():
    while True:
        try:
            user_input = input("\nUser > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        response = call_graph(user_input)
        print(f"\nBot: {response}")

main()