from .distances import distance_lat_long, haversine_distance
from .config import COUNT_POINT_IDS, FREE_SPEEDS, CELL_SIZE

def calculate_density_from_flow(countpointdf, free_speed):
    avg = sum(countpointdf['all_motor_vehicles']) / len(countpointdf['all_motor_vehicles'])
    density = avg / free_speed
    return [density, countpointdf['latitude'].values[0], countpointdf['longitude'].values[0]]

def point_density(data_frame, countpointids = COUNT_POINT_IDS):
    arr = []
    for id in countpointids:
        countdf = data_frame[data_frame['count_point_id'] == id]
        arr.append(calculate_density_from_flow(countdf, FREE_SPEEDS[id]))

    # Guess for bus density on bus only road and co ordinates of start of bus route and bus stop
    arr.append([6, 53.45927628199057, -2.2276463370981574])
    arr.append([6, 53.4645870298434, -2.2320827813567172])
    return arr

def number_of_cells(point_density_arr, cell_size = CELL_SIZE):
    arr = []
    for i in range(len(point_density_arr) - 1):
        print(i)
        d_actual = distance_lat_long(point_density_arr[i][1],point_density_arr[i][2],
                                     point_density_arr[i+1][1], point_density_arr[i+1][2])
        d_hav = haversine_distance(point_density_arr[i][1], point_density_arr[i][2],
                                   point_density_arr[i+1][1], point_density_arr[i+1][2])
        if 2 * d_hav < d_actual:
            d_actual = d_hav
        arr.append(int(d_actual // cell_size))
    return arr

def linear_density_gradient(point_density_arr, cell_arr):
    density_arr = []
    for i in range(len(point_density_arr) - 1):
        if i < 2: # allows for linear extrapolation from the last count point until the road
            # becomes bus only
            delta_p = (point_density_arr[i + 1][0] - point_density_arr[i][0]) / cell_arr[i]
        if i == 3: # sets density constant for bus only road section
            delta_p = 0
        for j in range(cell_arr[i]):
            density_arr.append(point_density_arr[i][0] + delta_p * j)
    return density_arr