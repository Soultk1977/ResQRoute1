# eta_calculator.py

from geopy.distance import geodesic

# backend/eta_calculator.py
def calculate_eta(current_location, destination, traffic_level, average_speed_kmph=40):
    distance_km = geodesic(current_location, destination).km
    
    # Convert traffic level to speed adjustment
    if traffic_level == "High":
        average_speed_kmph = 20
    elif traffic_level == "Medium":
        average_speed_kmph = 40
    elif traffic_level == "Low":
        average_speed_kmph = 60
    
    if average_speed_kmph == 0:
        return float('inf')  # Return infinite time if speed is zero
    
    eta_minutes = (distance_km / average_speed_kmph) * 60
    return round(eta_minutes, 2)

