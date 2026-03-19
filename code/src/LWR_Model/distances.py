import requests


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

def main():
    print(walk_lat_long(51.507351, -0.127758, 51.509865, -0.118853))

if __name__ == "__main__":
    main()
