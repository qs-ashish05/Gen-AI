import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_weather_details(city: str) -> dict:
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


def get_parameter_value(response: dict, parameter: str):
    """
    Returns the value of the given parameter from weather API response.
    Searches inside both 'location' and 'current' sections.
    """

    # Check inside location
    if parameter in response.get("location", {}):
        return response["location"][parameter]

    # Check inside current
    if parameter in response.get("current", {}):
        return response["current"][parameter]

    # Check inside condition (nested inside current)
    if parameter in response.get("current", {}).get("condition", {}):
        return response["current"]["condition"][parameter]

    return f"Parameter '{parameter}' not found"

info = get_weather_details("Mumbai")
res = get_parameter_value(info, "")
