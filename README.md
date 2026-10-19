# 🌿 Find the Better Moment

**Find a better time to travel, not just a route.**

Find the Better Moment is a real-time journey-planning prototype that compares possible departure windows using weather and route information, then recommends the highest-scoring option.

Instead of checking multiple sources and comparing times manually, users receive an explainable recommendation to help them make a more informed decision.

> **Current approach:** Rule-based scoring using external weather and route APIs. This prototype does not use a trained machine-learning model.

## 🎬 Demo

**[Watch the project demo](https://drive.google.com/file/d/1TREimnErzN-DpgqrvM37zIxFo6NgxSVA/view?usp=drive_link)**

<!-- Add a screenshot or GIF of the actual application here. -->

## ✨ Features

- **Departure-window comparison:** Evaluates candidate 30-minute time windows.
- **Weather context:** Incorporates weather information such as precipitation probability and wind speed.
- **Route information:** Uses route distance and estimated travel duration.
- **Explainable recommendations:** Returns a score and reasons for the selected window.
- **Comparative scoring:** Combines weather and route scores to rank candidate windows.
- **API-based architecture:** Separates the frontend, backend, external services, and scoring logic.

## ⚙️ How It Works

1. Enter an origin, destination, and available time range.
2. Generate candidate departure windows.
3. Retrieve the available weather and route information.
4. Calculate weather and route scores.
5. Combine the scores and rank the candidate windows.
6. Return the highest-scoring window with supporting information.

### Decision pipeline

```text
User Input
    ↓
Generate Time Windows
    ↓
Fetch Weather + Route Data
    ↓
Calculate Component Scores
    ↓
Combine and Rank Scores
    ↓
Recommended Departure Window
    ↓
Explanation of the Result
```

## 🧮 Scoring Approach

The current prototype uses configurable, rule-based heuristics.

The documented scoring formula is:

**Better Moment Score = 0.5 × Weather Score + 0.5 × Route Score**

- The weather score starts at 100 and is adjusted for factors including rain probability and wind speed.
- The route score is derived from estimated travel duration.
- The highest combined score determines the recommended window.

The weights are heuristic choices, not learned model parameters. The scores represent relative rankings within the prototype, not guaranteed travel quality or statistically validated probabilities.

## 🛠️ Technology Stack

| Component | Technologies |
|---|---|
| Frontend | React, Vite, JavaScript, CSS |
| Backend | Python, FastAPI, Pydantic |
| Weather data | Open-Meteo |
| Route data | SerpApi Google Maps Directions |

## 🚀 Run Locally

### Prerequisites

- Python 3.10+
- Node.js and npm
- A SerpApi API key

### 1. Clone the repository

```bash
git clone https://github.com/MithravindaU/find-the-better-moment.git
cd find-the-better-moment
```

### 2. Start the backend

```bash
cd backend
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `backend/.env` and add:

```env
SERPAPI_KEY=your_serpapi_key_here
```

Start the API:

```bash
python -m uvicorn main:app --reload
```

API documentation: `http://127.0.0.1:8000/docs`

### 3. Start the frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

If your local configuration uses a different backend URL, configure the frontend accordingly.

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Backend health check |
| POST | `/test-weather` | Test weather integration |
| POST | `/test-route` | Test route integration |
| POST | `/find-better-moment` | Generate a recommendation |

Example request:

```json
{
  "origin": "Vimal Jyothi Engineering College, Chemperi",
  "destination": "Taliparamba",
  "start_time": "16:00",
  "end_time": "18:30"
}
```

The main endpoint returns a recommended time window, its score, route and weather information, and supporting reasons. See the API documentation for the actual response schema.

## 📁 Repository Structure

```text
find-the-better-moment/
├── backend/
│   ├── api/
│   ├── engine/
│   ├── services/
│   └── main.py
├── frontend/
│   ├── public/
│   └── src/
├── 01-problem-discovery.md
├── 02-user-journey.md
└── README.md
```

## ⚠️ Current Limitations

- Scoring is rule-based, not machine-learned.
- Recommendation quality depends on the availability and freshness of external API data.
- The ranking weights and thresholds have not been established as optimal.
- A score or ranking separation does not guarantee a better real-world experience.
- Crowd levels, personal preferences, safety, and destination atmosphere are not established as implemented scoring inputs.

## 🗺️ Future Directions

- Personal preference-based scoring.
- More weather and travel-condition signals.
- Better handling of missing or stale data.
- Automated tests and evaluation against real user feedback.
- Broader experience planning beyond departure-time recommendations.

These are proposed improvements, not claims about current functionality.

## 🔐 Security

- Keep API keys in environment variables.
- Never commit real credentials or `.env` files.
- Use an `.env.example` file containing placeholder values.
- Configure production secrets through the deployment platform.

## 👩‍💻 Author

**Mithravinda U**

[GitHub](https://github.com/MithravindaU)

---

*Built to explore how changing real-world conditions can support clearer, more informed everyday decisions.*
