import datetime

def predict_traffic_density(current_location=None):
    # Get the current hour of the day (24-hour format)
    time_of_day = datetime.datetime.now().hour

    if 7 <= time_of_day <= 10 or 17 <= time_of_day <= 20:
        return "High"
    elif 11 <= time_of_day <= 16:
        return "Moderate"
    else:
        return "Low"
