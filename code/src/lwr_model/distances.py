import requests
import math

def distance_lat_long(lat1, lon1, lat2, lon2):
    osrm_url = f"https://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}"
    params = {"overview": "full", "geometries": "geojson"}
    osrm_req = requests.get(osrm_url, params=params)
    osrm_data = osrm_req.json()
    route = osrm_data['routes'][0]
    distance = route['distance']
    return distance


def walk_lat_long(lat1, lon1, lat2, lon2):
    osrm_url = f"https://router.project-osrm.org/route/v1/walking/{lon1},{lat1};{lon2},{lat2}"
    params = {"overview": "full", "geometries": "geojson"}
    osrm_req = requests.get(osrm_url, params=params)
    osrm_data = osrm_req.json()
    route = osrm_data['routes'][0]
    distance = route['distance']
    return distance

def haversine_distance(lat1, lon1, lat2, lon2):
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 6371 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) * 1000

def main():
    print(walk_lat_long(51.507351, -0.127758, 51.509865, -0.118853))

if __name__ == "__main__":
    main()
