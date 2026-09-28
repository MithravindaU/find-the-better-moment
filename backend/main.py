from services.time_service import generate_time_windows

from engine.better_moment import (
    calculate_weather_score,
    calculate_route_score,
    calculate_better_moment_score,
    explain_better_moment,
    calculate_confidence
)


from services.route_service import get_route_at_time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.weather_service import get_weather

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TripRequest(BaseModel):
    origin: str
    destination: str
    start_time: str
    end_time: str


@app.get("/")
def home():
    return {
        "message": "Find the Better Moment API is running!"
    }


@app.post("/test-weather")
def test_weather():

    # Temporary coordinates for testing
    latitude = 12.9667
    longitude = 75.3500

    weather = get_weather(latitude, longitude)

    if weather is None:
        return {
            "error": "Weather API failed"
        }

    return {
        "message": "Weather API connected!",
        "latitude": latitude,
        "longitude": longitude,
        "weather": weather
    }

@app.post("/test-route")
def test_route():

    origin = "Vimal Jyothi Engineering College, Chemperi"
    destination = "Taliparamba"

    from datetime import datetime, timedelta

    departure_time = datetime.now() + timedelta(hours=1)
    timestamp = int(departure_time.timestamp())

    route = get_route_at_time(
        origin,
        destination,
        timestamp
    )

    if route is None:
        return {
            "error": "Route API failed"
        }

    directions = route.get("directions", [])

    if not directions:
        return {
            "error": "No route found"
        }

    first_route = directions[0]

    return {
        "message": "SerpApi route connected!",
        "origin": origin,
        "destination": destination,
        "distance": first_route.get("formatted_distance"),
        "duration": first_route.get("formatted_duration"),
        "typical_duration": first_route.get("typical_duration_range")
    }

@app.post("/find-better-moment")
def find_better_moment(request: TripRequest):

    # 1. Generate time windows
    windows = generate_time_windows(
        request.start_time,
        request.end_time
    )

    # 2. Get weather ONCE
    latitude = 12.9667
    longitude = 75.3500

    weather = get_weather(latitude, longitude)

    if weather is None:
        return {"error": "Weather API failed"}

    hourly = weather["hourly"]

    results = []

    # 3. Check each time window
    for window in windows:

        target_hour = int(window["start"].split(":")[0])

        weather_data = None

        for i, time_value in enumerate(hourly["time"]):

            api_hour = int(time_value.split("T")[1].split(":")[0])

            if api_hour == target_hour:
                weather_data = {
                    "temperature": hourly["temperature_2m"][i],
                    "rain_probability": hourly["precipitation_probability"][i],
                    "wind_speed": hourly["wind_speed_10m"][i]
                }
                break

        if weather_data is None:
            continue

        # 4. Route for this time
        from datetime import datetime

        departure = datetime.now().replace(
            hour=target_hour,
            minute=0,
            second=0,
            microsecond=0
        )

        timestamp = int(departure.timestamp())

        route = get_route_at_time(
            request.origin,
            request.destination,
            timestamp
        )

        if route is None:
            continue

        directions = route.get("directions", [])

        if not directions:
            continue

        first_route = directions[0]

        duration_text = first_route.get(
            "formatted_duration"
        )

        distance = first_route.get(
            "formatted_distance"
        )

        # 5. Convert duration
        duration_minutes = 0

        if "hr" in duration_text:
            hours = int(
                duration_text.split("hr")[0].strip()
            )
            duration_minutes += hours * 60

        if "min" in duration_text:
            remaining = duration_text.split("hr")[-1]
            number = remaining.replace("min", "").strip()

            if number:
                duration_minutes += int(number)

        # 6. Scores
        weather_score = calculate_weather_score(
            weather_data["rain_probability"],
            weather_data["wind_speed"]
        )

        route_score = calculate_route_score(
            duration_minutes
        )

        better_moment_score = calculate_better_moment_score(
            route_score,
            weather_score
        )

        results.append({
            "start": window["start"],
            "end": window["end"],
            "temperature": weather_data["temperature"],
            "rain_probability": weather_data["rain_probability"],
            "wind_speed": weather_data["wind_speed"],
            "distance": distance,
            "travel_duration": duration_text,
            "weather_score": weather_score,
            "route_score": route_score,
            "better_moment_score": better_moment_score
        })

    # 7. Make sure we have results
    if not results:
        return {
            "error": "Could not evaluate any time windows"
        }

    # 8. Find best window
    best_window = max(
        results,
        key=lambda x: x["better_moment_score"]
    )

    scores = [
        item["better_moment_score"]
        for item in results
    ]

    confidence = calculate_confidence(scores)

    reasons = explain_better_moment(
        best_window["rain_probability"],
        best_window["wind_speed"],
        best_window["route_score"]
    )

    return {
        "message": "Better Moment found!",
        "best_window": (
            f"{best_window['start']}–{best_window['end']}"
        ),
        "score": best_window["better_moment_score"],
        "confidence": confidence,
        "travel_duration": best_window["travel_duration"],
        "distance": best_window["distance"],
        "rain_probability": best_window["rain_probability"],
        "wind_speed": best_window["wind_speed"],
        "reasons": reasons,
        "all_windows": results
    }