import json
import requests
from dotenv import load_dotenv
from openai import OpenAI
import os
from langsmith.wrappers import wrap_openai
from langsmith import traceable

load_dotenv()

client = wrap_openai(OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
))
# base url - https://api.weatherapi.com/v1
# refrence - https://www.weatherapi.com/docs/

@traceable
def get_weather(city: str) -> dict:
    print("Tool Called: get_weather", city)
    try:
        base_url = os.getenv("WEATHER_API_BASE_URL")
        api_key = os.getenv("WEATHER_API_KEY")

        if not base_url or not api_key:
            raise ValueError("API base URL or API key is missing in .env file")

        url = f"{base_url}/current.json"

        params = {
            "key": api_key,
            "q": city,
            "aqi": "no",
            "pollen": "no"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses

        return response.json()  # Full weather details

    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return {}
    except Exception as e:
        print(f"Error: {e}")
        return {}

@traceable
def run_command(command):
    result = os.system(command=command)
    return result

# we can have more than one avaialble tools 
avaiable_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as an input and returns the current weather for the city"
    },
    "run command":{
        "fn": run_command,
        "description": "Takes a command as an input and executes that command in your local machine"
    }
}

system_prompt = f"""
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You work on start, plan, action, observe mode.
    For the given user query and available tools, plan the step by step execution, based on the planning,
    select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    Output JSON Format:
    {{
        "step": "string",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }}

    Available Tools:
    - get_weather: Takes a city name as an input and returns the current weather for the city
    - run command: Takes a command as an input and executes that command in your local machine
    
    Example:
    User Query: What is the weather of new york?
    Output: {{ "step": "plan", "content": "The user is interseted in weather data of new york" }}
    Output: {{ "step": "plan", "content": "From the available tools I should call get_weather" }}
    Output: {{ "step": "action", "function": "get_weather", "input": "new york" }}
    Output: {{ "step": "observe", "output": "12 Degree Cel" }}
    Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees." }}
"""

messages = [
    { "role": "system", "content": system_prompt }
]

while True:
    user_query = input('User > ')
    messages.append({ "role": "user", "content": user_query })

    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=messages
        )

        parsed_output = json.loads(response.choices[0].message.content)
        messages.append({ "role": "assistant", "content": json.dumps(parsed_output) })

        if parsed_output.get("step") == "plan":
            print(f"Processing: {parsed_output.get('content')}")
            continue
        
        if parsed_output.get("step") == "action":
            tool_name = parsed_output.get("function")
            tool_input = parsed_output.get("input")

            if avaiable_tools.get(tool_name, False) != False:
                output = avaiable_tools[tool_name].get("fn")(tool_input)
                messages.append({ "role": "assistant", "content": json.dumps({ "step": "observe", "output":  output}) })
                continue
        
        if parsed_output.get("step") == "output":
            print(f"Bot > {parsed_output.get('content')}")
            break