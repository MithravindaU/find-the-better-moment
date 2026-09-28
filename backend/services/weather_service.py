import requests


def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation_probability,weather_code,wind_speed_10m",
        "forecast_days": 1,
        "timezone": "auto"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        if response.status_code != 200:
            print("Weather API error:", response.status_code)
            print(response.text)
            return None

        return response.json()

    except requests.RequestException as error:
        print("Weather connection error:", error)
        return None