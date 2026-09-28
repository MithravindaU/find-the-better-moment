def calculate_weather_score(rain_probability, wind_speed):

    score = 100

    if rain_probability > 70:
        score -= 50
    elif rain_probability > 40:
        score -= 25
    elif rain_probability > 20:
        score -= 10

    if wind_speed > 30:
        score -= 20
    elif wind_speed > 20:
        score -= 10

    return max(0, score)


def calculate_route_score(duration_minutes):

    score = 100 - (duration_minutes / 60 * 50)

    return max(0, min(100, score))


def calculate_better_moment_score(route_score, weather_score):

    score = (
        0.5 * route_score +
        0.5 * weather_score
    )

    return round(score, 2)


def explain_better_moment(rain_probability, wind_speed, route_score):

    reasons = []

    if rain_probability <= 20:
        reasons.append("Low rain probability")
    elif rain_probability <= 40:
        reasons.append("Moderate rain probability")
    else:
        reasons.append("Higher rain probability")

    if wind_speed <= 20:
        reasons.append("Low wind")
    else:
        reasons.append("Higher wind")

    if route_score >= 70:
        reasons.append("Good travel conditions")
    elif route_score >= 50:
        reasons.append("Moderate travel conditions")
    else:
        reasons.append("Longer travel time")

    return reasons


def calculate_confidence(scores):

    if len(scores) < 2:
        return 50

    sorted_scores = sorted(scores, reverse=True)

    gap = sorted_scores[0] - sorted_scores[1]

    if gap >= 20:
        return 95
    elif gap >= 10:
        return 85
    elif gap >= 5:
        return 75
    elif gap >= 2:
        return 65
    else:
        return 55