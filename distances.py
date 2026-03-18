naptan_url = "https://naptan.api.dft.gov.uk/v1/access-nodes?atcoAreaCodes=180&dataFormat=csv"

import requests
import pandas as pd
import io

naptan_req = requests.get(naptan_url)
print(naptan_req.status_code)

bus_stops = pd.read_csv(io.StringIO(naptan_req.text))


langley_road = bus_stops[(bus_stops['ATCOCode'] == '1800EB07851') & (bus_stops['Status'] == 'active')]
university = bus_stops[(bus_stops['ATCOCode'] == '1800SB30651') & (bus_stops['Status'] == 'active')]

def distance_lat_long(lat1, lon1, lat2, lon2):
    print(f"{lon1},{lat1},{lon2},{lat2}")
    osrm_url = f"https://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}"
    params = {"overview": "full", "geometries": "geojson"}
    osrm_req = requests.get(osrm_url, params=params)
    osrm_data = osrm_req.json()
    route = osrm_data['routes'][0]
    distance = route['distance']
    return distance

print(distance_lat_long(langley_road['Latitude'].values[0], langley_road['Longitude'].values[0], university['Latitude'].values[0], university['Longitude'].values[0]))


