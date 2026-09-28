from datetime import datetime, timedelta


def generate_time_windows(start_time, end_time, interval_minutes=30):

    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")

    windows = []
    current = start

    while current < end:

        next_time = current + timedelta(minutes=30)

        if next_time <= end:
            windows.append({
                "start": current.strftime("%H:%M"),
                "end": next_time.strftime("%H:%M")
            })

        current += timedelta(minutes=interval_minutes)

    return windows