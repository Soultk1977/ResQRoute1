# gps_tracker.py

import random

# Simulates GPS coordinates of emergency vehicles
def get_vehicle_location(vehicle_id):
    # Dummy coordinates (latitude, longitude) near Delhi
    locations = {
        "AMB001": (28.644800, 77.216721),
        "FIRE002": (28.654200, 77.202400),
        "POL003": (28.630400, 77.218800)
    }
    return locations.get(vehicle_id, (28.600000 + random.random(), 77.200000 + random.random()))
