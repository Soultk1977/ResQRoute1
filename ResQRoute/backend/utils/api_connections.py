import time
import random

def get_mock_location(vehicle_id):
    # Simulate GPS coordinates for testing
    return {
        "vehicle_id": vehicle_id,
        "latitude": round(random.uniform(28.60, 28.70), 6),
        "longitude": round(random.uniform(77.10, 77.30), 6),
        "timestamp": time.time()
    }

def override_signal(signal_id):
    # Simulate successful signal override
    return {
        "signal_id": signal_id,
        "status": "green",
        "override": True
    }
