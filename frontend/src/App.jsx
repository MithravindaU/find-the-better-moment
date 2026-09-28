import { useState } from "react";
import "./App.css";

function App() {
  const [origin, setOrigin] = useState("");
  const [destination, setDestination] = useState("");
  const [startTime, setStartTime] = useState("16:00");
  const [endTime, setEndTime] = useState("18:30");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const findBetterMoment = async () => {
    if (!origin || !destination) {
      setError("Tell us where you're starting and where you're heading.");
      return;
    }

    if (startTime >= endTime) {
      setError("Your ending time should be later than your starting time.");
      return;
    }

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/find-better-moment",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            origin,
            destination,
            start_time: startTime,
            end_time: endTime,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok || data.error) {
        throw new Error(data.error || "Something went wrong.");
      }

      setResult(data);

      setTimeout(() => {
        document
          .querySelector(".result")
          ?.scrollIntoView({
            behavior: "smooth",
            block: "start",
          });
      }, 100);
    } catch (err) {
      console.error(err);
      setError(
        "We couldn't find your moment. Make sure the backend is running and try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="ambient ambient-one"></div>
      <div className="ambient ambient-two"></div>
      <div className="grain"></div>

      {/* HEADER */}
      <header className="topbar">
        <div className="brand">
          <span className="brand-dot"></span>
          better moment
        </div>

        <div className="tiny-note">
          for days worth stepping outside
        </div>
      </header>

      <main>
        {/* HERO */}
        <section className="hero">
          <div className="eyebrow">
            <span>✦</span>
            A little help with the timing
          </div>

          <h1>
            Find your
            <em> better moment.</em>
          </h1>

          <p className="hero-copy">
            The weather changes.
            <br />
            The roads change.
            <br />
            Maybe your timing should too.
          </p>

          <div className="scroll-hint">
            <span></span>
            plan a little moment
          </div>
        </section>

        {/* PLANNER */}
        <section className="planner">
          <div className="planner-heading">
            <div>
              <span className="section-number">01</span>
              <h2>Where are you going?</h2>
            </div>

            <span className="soft-caption">
              we'll look at the little things
            </span>
          </div>

          <div className="journey">
            <div className="journey-line">
              <span className="journey-point start"></span>
              <span className="journey-stem"></span>
              <span className="journey-point end"></span>
            </div>

            <div className="journey-fields">
              <div className="location-field">
                <label>STARTING FROM</label>

                <input
                  value={origin}
                  onChange={(e) => {
                    setOrigin(e.target.value);
                    setError("");
                  }}
                  placeholder="Where will you begin?"
                  autoComplete="off"
                />
              </div>

              <div className="location-field">
                <label>HEADING TO</label>

                <input
                  value={destination}
                  onChange={(e) => {
                    setDestination(e.target.value);
                    setError("");
                  }}
                  placeholder="Where would you like to go?"
                  autoComplete="off"
                />
              </div>
            </div>
          </div>

          {/* TIME */}
          <div className="timing-heading">
            <div>
              <span className="section-number">02</span>
              <h2>When are you free?</h2>
            </div>

            <span className="soft-caption">
              we'll find the sweet spot
            </span>
          </div>

          <div className="time-picker">
            <div className="time-card">
              <span>FROM</span>

              <input
                type="time"
                value={startTime}
                onChange={(e) => {
                  setStartTime(e.target.value);
                  setError("");
                }}
              />
            </div>

            <div className="time-arrow">→</div>

            <div className="time-card">
              <span>UNTIL</span>

              <input
                type="time"
                value={endTime}
                onChange={(e) => {
                  setEndTime(e.target.value);
                  setError("");
                }}
              />
            </div>
          </div>

          <div className="timeline">
            <div className="timeline-line"></div>

            <span className="timeline-dot left"></span>
            <span className="timeline-dot middle"></span>
            <span className="timeline-dot right"></span>

            <span className="timeline-label left-label">
              your window
            </span>

            <span className="timeline-label right-label">
              we'll explore it
            </span>
          </div>

          {/* ERROR */}
          {error && (
            <div className="error-message" role="alert">
              <span>♡</span>
              <p>{error}</p>
            </div>
          )}

          {/* BUTTON */}
          <button
            className={`moment-button ${
              loading ? "is-loading" : ""
            }`}
            onClick={findBetterMoment}
            disabled={loading}
          >
            <span>
              {loading
                ? "Looking through your window..."
                : "Find my better moment"}
            </span>

            <span className="button-circle">
              {loading ? (
                <span className="loading-dots">
                  <i></i>
                  <i></i>
                  <i></i>
                </span>
              ) : (
                "↗"
              )}
            </span>
          </button>

          <p className="promise">
            No complicated planning. Just a little better timing.
          </p>
        </section>

        {/* RESULT */}
        {result && (
          <section className="result">
            <div className="result-intro">
              <span className="eyebrow">
                <span>✦</span>
                we found something
              </span>

              <h2>
                This feels like
                <em> your moment.</em>
              </h2>

              <p className="result-subtitle">
                Out of the moments you gave us, this one has the
                nicest little balance.
              </p>
            </div>

            {/* BEST MOMENT */}
            <div className="moment-card">
              <div className="moment-top">
                <div>
                  <span className="moment-label">
                    YOUR BETTER WINDOW
                  </span>

                  <h3>{result.best_window}</h3>

                  <p>
                    The conditions line up a little better here.
                  </p>
                </div>

                <div className="moment-score">
                  <strong>{result.score}</strong>
                  <span>moment score</span>
                </div>
              </div>

              {/* DETAILS */}
              <div className="moment-details">
                <div>
                  <span>🌦</span>
                  <strong>{result.rain_probability}%</strong>
                  <small>chance of rain</small>
                </div>

                <div>
                  <span>𓂃</span>
                  <strong>{result.wind_speed} km/h</strong>
                  <small>wind</small>
                </div>

                <div>
                  <span>↗</span>
                  <strong>{result.travel_duration}</strong>
                  <small>travel time</small>
                </div>

                <div>
                  <span>⌁</span>
                  <strong>{result.distance}</strong>
                  <small>distance</small>
                </div>
              </div>

              {/* REASONS */}
              <div className="reasons">
                <span className="reason-title">
                  little reasons...
                </span>

                {result.reasons.map((reason, index) => (
                  <span className="reason-pill" key={index}>
                    {reason}
                  </span>
                ))}
              </div>

              {/* CONFIDENCE */}
              <div className="confidence">
                <div className="confidence-heading">
                  <span>how clear was the choice?</span>
                  <strong>{result.confidence}%</strong>
                </div>

                <div className="confidence-track">
                  <span
                    style={{
                      width: `${result.confidence}%`,
                    }}
                  ></span>
                </div>

                <p>
                  Based on how clearly this window stood apart
                  from the others we considered.
                </p>
              </div>
            </div>

            {/* COMPARISON */}
            <div className="explore">
              <div className="explore-heading">
                <div>
                  <span className="section-number">03</span>
                  <h2>The moments we considered</h2>
                </div>

                <span className="soft-caption">
                  every window tells a little story
                </span>
              </div>

              <div className="moment-list">
                {result.all_windows.map((window, index) => {
                  const isBest =
                    window.start ===
                    result.best_window.split("–")[0];

                  return (
                    <div
                      className={`moment-row ${
                        isBest ? "best-row" : ""
                      }`}
                      key={index}
                    >
                      <div className="row-time">
                        {window.start}
                        <span>– {window.end}</span>
                      </div>

                      <div className="row-condition">
                        <span
                          style={{
                            width: `${window.better_moment_score}%`,
                          }}
                        ></span>
                      </div>

                      <div className="row-score">
                        {window.better_moment_score}
                      </div>
                    </div>
                  );
                })}
              </div>

              <p className="comparison-note">
                Each bar represents the overall conditions for
                that time window.
              </p>
            </div>

            <div className="closing-note">
              <span>✦</span>
              Sometimes the best plan is simply better timing.
            </div>
          </section>
        )}
      </main>

      <footer>
        <span>better moment</span>
        <span>made for going somewhere</span>
      </footer>
    </div>
  );
}

export default App;