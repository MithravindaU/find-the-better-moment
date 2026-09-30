# 🌿 Find the Better Moment

### Real-time decision support for better-timed everyday journeys.

> **The best time to go isn't always the first time you think of.**

Find the Better Moment is a real-time decision-support application that evaluates multiple possible time windows for a journey and identifies a more suitable moment based on changing environmental and travel conditions.

Instead of simply answering:

**"Can I go?"**

the system asks:

**"When would it be better to go?"**

---

## ✨ The Idea

Everyday journeys are influenced by conditions that change throughout the day.

A route might be available at 4:00 PM, but weather conditions, wind, or travel conditions may be different at 5:00 PM.

Most existing tools present these pieces of information separately:

- 🌦️ Weather applications provide weather information
- 🗺️ Navigation applications provide route information
- ⏰ Scheduling applications provide available time

**Find the Better Moment brings these changing factors together and evaluates the user's entire available time window.**

The system generates possible departure windows, gathers real-time data for each window, scores the conditions, and recommends the window with the highest overall score.

---

# 🎯 Problem Statement

When planning a journey, users often choose a departure time based on habit or convenience.

However, conditions such as:

- 🌧️ Rain probability
- 💨 Wind
- 🚗 Travel conditions
- 🕐 Time availability

can change throughout the day.

The problem is not always **finding a route**.

The problem is often **finding a better time to take that route**.

---

# 💡 Solution

Find the Better Moment treats **time itself as something that can be optimized**.

The user provides:

1. Starting location
2. Destination
3. Available start time
4. Available end time

The system then:

1. Divides the available period into 30-minute windows.
2. Retrieves weather conditions for the relevant times.
3. Retrieves route information for each departure window.
4. Calculates separate weather and route scores.
5. Combines them into a Better Moment Score.
6. Compares all candidate windows.
7. Identifies the highest-scoring window.
8. Explains why that window was selected.

---

# 🧠 How It Works

```text
                    USER
                      │
                      ▼
        ┌─────────────────────────┐
        │   Journey Information   │
        │                         │
        │ Origin                  │
        │ Destination             │
        │ Available Time Window   │
        └────────────┬────────────┘
                     │
                     ▼
          Generate Time Windows
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   ┌──────────────┐      ┌──────────────┐
   │   Weather    │      │    Route     │
   │   Open-Meteo │      │   SerpApi    │
   └──────┬───────┘      └──────┬───────┘
          │                     │
          └──────────┬──────────┘
                     ▼
          ┌────────────────────┐
          │ Better Moment      │
          │ Engine             │
          │                    │
          │ Weather Score      │
          │ Route Score        │
          │ Combined Score     │
          └──────────┬─────────┘
                     │
                     ▼
             Compare Windows
                     │
                     ▼
          ┌────────────────────┐
          │ Recommended Window │
          │                    │
          │ Score              │
          │ Conditions         │
          │ Reasons            │
          │ Confidence         │
          └────────────────────┘
```

---

# 🌦️ Real-Time Data Sources

## Weather

**Open-Meteo** provides hourly weather information used by the decision engine, including:

- Temperature
- Precipitation probability
- Weather conditions
- Wind speed

## 🗺️ Route Information

**SerpApi Google Maps Directions** provides route information for candidate departure times, including:

- Distance
- Travel duration
- Departure-time route information

---

# ✨ Key Features

### 🕐 Time Window Analysis

Instead of evaluating only one departure time, the system examines multiple possible windows within the user's availability.

### 🌦️ Live Weather Context

Weather conditions are incorporated into the decision rather than displayed separately.

### 🗺️ Departure-Time Route Analysis

Route information is requested for individual candidate departure times.

### 🧠 Explainable Decision Engine

The system provides reasons behind the recommendation instead of returning only a number.

### 📊 Window Comparison

Users can see how the different candidate windows compare.

### 🎯 Confidence Indicator

A heuristic confidence value is generated from the difference between the highest and second-highest scores.

> Confidence is currently a heuristic indicator, not a statistically calibrated probability.

### 🎨 Calm, Human-Centered Interface

The frontend uses a soft, minimal visual language designed to make planning feel simple rather than dashboard-heavy.

---

# 🧮 Better Moment Engine

The current version uses a transparent rule-based scoring engine.

This makes the recommendation explainable instead of treating the result as a black box.

### Weather Score

The weather score starts at `100` and is adjusted according to:

- Rain probability
- Wind speed

Higher rain probability and stronger wind reduce the score.

### Route Score

The route score is derived from estimated travel duration.

Shorter travel durations receive a higher score.

### Final Score

The current prototype combines the two scores:

```text
Better Moment Score
        =
0.5 × Weather Score
+
0.5 × Route Score
```

The window with the highest resulting score becomes the recommended window.

> The weights and thresholds are configurable heuristic rules rather than learned model parameters.

---

# 🎯 Example

Suppose a user is available between:

```text
16:00 → 18:30
```

The system generates:

```text
16:00 → 16:30
16:30 → 17:00
17:00 → 17:30
17:30 → 18:00
18:00 → 18:30
```

Each window is evaluated independently.

Example:

| Time Window | Rain | Wind | Weather Score | Route Score | Better Moment Score |
|-------------|------|------|---------------|-------------|---------------------|
| 16:00–16:30 | 41% | 11.1 km/h | 75 | 54.17 | 64.58 |
| 16:30–17:00 | 41% | 11.1 km/h | 75 | 54.17 | 64.58 |
| 17:00–17:30 | 43% | 8.8 km/h | 75 | 54.17 | 64.58 |
| 17:30–18:00 | 43% | 8.8 km/h | 75 | 54.17 | 64.58 |
| **18:00–18:30** | **33%** | **6.6 km/h** | **90** | **54.17** | **72.08** |

The system identifies:

```text
18:00–18:30
```

as the highest-scoring window in this example.

---

# 🛠️ Technology Stack

## Frontend

- React
- Vite
- JavaScript
- CSS

## Backend

- Python
- FastAPI
- Pydantic

## APIs

- Open-Meteo
- SerpApi Google Maps Directions

## Development

- Git
- GitHub
- VS Code
- Google Colab for experimentation

---

# 📁 Project Structure

```text
find-the-better-moment/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── api/
│   ├── services/
│   │   ├── serpapi_service.py
│   │   ├── weather_service.py
│   │   ├── route_service.py
│   │   └── time_service.py
│   ├── engine/
│   │   └── better_moment.py
│   └── main.py
│
├── data/
├── notebooks/
├── screenshots/
├── demo/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have:

- Python 3.10+
- Node.js
- npm
- Git

You will also need a SerpApi API key.

## 1. Clone the Repository

```bash
git clone https://github.com/MithravindaU/find-the-better-moment.git
cd find-the-better-moment
```

## 2. Backend Setup

```bash
cd backend
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 3. Configure Environment Variables

Create:

```text
backend/.env
```

Add:

```env
SERPAPI_KEY=your_serpapi_key_here
```

Never commit your real API key to GitHub.

Keep `.env` in `.gitignore`.

Use `.env.example` to show the required environment-variable structure:

```env
SERPAPI_KEY=
```

## 4. Start the Backend

From the `backend` directory:

```bash
python -m uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## 5. Start the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🔌 API Endpoints

### `GET /`

Basic backend health check.

### `POST /test-weather`

Tests the weather API connection.

### `POST /test-route`

Tests the SerpApi route connection.

### `POST /find-better-moment`

Main decision endpoint.

Example request:

```json
{
  "origin": "Vimal Jyothi Engineering College, Chemperi",
  "destination": "Taliparamba",
  "start_time": "16:00",
  "end_time": "18:30"
}
```

Example response:

```json
{
  "message": "Better Moment found!",
  "best_window": "18:00–18:30",
  "score": 72.08,
  "confidence": 75,
  "travel_duration": "55 min",
  "distance": "30.8 km",
  "rain_probability": 33,
  "wind_speed": 6.6,
  "reasons": [
    "Moderate rain probability",
    "Low wind",
    "Moderate travel conditions"
  ]
}
```

---

# 🔄 Decision Pipeline

```text
Input
  │
  ├── Origin
  ├── Destination
  ├── Start Time
  └── End Time
        │
        ▼
Generate 30-Minute Windows
        │
        ▼
Fetch Weather Conditions
        │
        ▼
Fetch Route Conditions
        │
        ▼
Calculate Weather Score
        │
        ▼
Calculate Route Score
        │
        ▼
Calculate Combined Score
        │
        ▼
Compare All Windows
        │
        ▼
Select Highest Score
        │
        ▼
Generate Explanation
        │
        ▼
Return Better Moment
```

---

# 🌱 Why This Approach?

The project is designed around **decision support rather than information overload**.

Instead of showing users several unrelated numbers and asking them to interpret everything themselves, the system combines available signals into a decision-oriented result while still showing the underlying factors.

The architecture is modular, allowing additional signals to be introduced later without redesigning the entire application.

---

# 🔮 Future Improvements

### 📍 Dynamic Location Intelligence

Use geocoding to obtain the actual coordinates of the user's origin and destination instead of relying on predefined coordinates.

### 🌧️ More Weather Factors

Potential additions include:

- Temperature
- Precipitation intensity
- Visibility
- Weather severity
- Hourly forecasts

### 🚦 Richer Travel Conditions

Add more route and traffic-related signals where reliable real-time data is available.

### 🧠 Adaptive Scoring

Future versions could learn how different users prioritize:

- Speed
- Weather
- Comfort
- Cost
- Reliability

### 🧩 More Decision Domains

The same engine could eventually evaluate moments for:

- 🚶 Walking
- 🚴 Cycling
- 🏃 Outdoor activities
- 🛍️ Errands
- 📸 Photography
- 🌳 Outdoor plans
- ☕ Short trips

The core idea remains the same:

> **Find the better moment, not just the available moment.**

---

# 📊 Current Project Status

| Component | Status |
|-----------|--------|
| Core concept | ✅ |
| FastAPI backend | ✅ |
| Weather integration | ✅ |
| Route integration | ✅ |
| Time-window generation | ✅ |
| Scoring engine | ✅ |
| Explainable results | ✅ |
| React frontend | ✅ |
| Frontend-backend integration | ✅ |
| Dynamic geolocation | 🔄 |
| Production deployment | 🔄 |
| Final UI polish | 🔄 |
| Demo video | 🔄 |

---

# 🔐 Security

API credentials are stored using environment variables.

Never commit:

```text
.env
```

or any real API key.

Use:

```text
.env.example
```

to document required environment variables.

---


# 🎥 Demo

> Demo video and live deployment will be added here.

**Live Demo:** Coming soon

**Demo Video:** Coming soon

---

# 📌 Project Philosophy

We don't always need more information.

Sometimes we just need to know **when the moment is better**.


# 👥 Contributer

- Mithravinda U
  
**Find the Better Moment**

Built as a real-time decision-support project exploring how changing real-world conditions can be combined to improve everyday decisions.
---

🌿 **Find the Better Moment**
