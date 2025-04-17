import streamlit as st
from backend.gps_tracker import get_vehicle_location
from backend.find_nearest_service import find_nearest_service
from backend.eta_calculator import calculate_eta
from backend.traffic_predictor import predict_traffic_density

# 🏥 Emergency services data (mocked for now)
services_dict = {
    "Ambulance": [
        {"name": "Apollo Hospital", "location": (28.6353, 77.2250)},
        {"name": "AIIMS", "location": (28.5665, 77.2100)},
    ],
    "Fire Brigade": [
        {"name": "Karol Bagh Fire Station", "location": (28.6514, 77.1908)},
        {"name": "Connaught Place Fire Station", "location": (28.6315, 77.2167)},
    ],
    "Police": [
        {"name": "Karol Bagh Police Station", "location": (28.6521, 77.1893)},
        {"name": "CP Police Station", "location": (28.6300, 77.2190)},
    ]
}

# 🟢 Dummy data just for vehicle type detection
def get_vehicle_type(vehicle_id):
    vehicle_id = vehicle_id.lower()
    if "amb" in vehicle_id:
        return "Ambulance"
    elif "fire" in vehicle_id:
        return "Fire Brigade"
    elif "police" in vehicle_id or "pol" in vehicle_id:
        return "Police"
    return "Unknown"


# 🔍 Display vehicle status
def display_vehicle_status(vehicle_id):
    st.subheader("🚑 Vehicle Live Status")

    location = get_vehicle_location(vehicle_id)
    vehicle_type = get_vehicle_type(vehicle_id)

    st.write(f"**Vehicle ID:** {vehicle_id}")
    st.write(f"**Vehicle Type:** {vehicle_type}")
    st.write(f"**Current Location:** `{location}`")

    # Emergency Finder
    services = services_dict.get(vehicle_type, [])
    nearest_service = find_nearest_service(location, services)

    if nearest_service:
        destination_name = nearest_service['name']
        destination_coords = nearest_service['location']
    else:
        destination_name = "Not found"
        destination_coords = (0, 0)

    st.write(f"**Nearest Destination:** {destination_name}")
    st.write(f"**Destination Coordinates:** `{destination_coords}`")

    # Predict traffic
    traffic_level = predict_traffic_density(location)
    st.write(f"**Predicted Traffic Level:** {traffic_level}")

    # ETA Calculation
    eta = calculate_eta(location, destination_coords, traffic_level)
    st.write(f"**Estimated Time of Arrival (ETA):** `{eta} minutes`")
