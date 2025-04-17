import math

def calculate_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

def find_nearest_service(vehicle_location, services):
    min_distance = float('inf')
    nearest_service = None
    for service in services:
        distance = calculate_distance(vehicle_location, service['location'])
        if distance < min_distance:
            min_distance = distance
            nearest_service = service
    return nearest_service
