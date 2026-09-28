import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_route_at_time(origin, destination, departure_timestamp):

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_maps_directions",
        "start_addr": origin,
        "end_addr": destination,
        "travel_mode": "0",
        "time": f"depart_at:{departure_timestamp}",
        "api_key": os.getenv("SERPAPI_KEY")
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("SerpApi error:", response.text)
        return None

    return response.json()