from .distances import distance_lat_long, haversine_distance
from .config import COUNT_POINT_IDS, FREE_SPEEDS, CELL_SIZE
from .data import clean_count_data

def calculate_density_from_flow(countpointdf, free_speed):
    avg = sum(countpointdf['all_motor_vehicles']) / len(countpointdf['all_motor_vehicles'])
    density = avg / free_speed
    density=density/1000
    return [density, countpointdf['latitude'].values[0], countpointdf['longitude'].values[0]]

def point_density(data_frame, countpointids = COUNT_POINT_IDS):
    arr = []
    for id in countpointids:
        v_free = FREE_SPEEDS[id] * (1000/3600)  # km/h → m/s
        countdf = data_frame[data_frame['count_point_id'] == id]
        arr.append(calculate_density_from_flow(countdf, v_free))

    # Guess for bus density on bus only road and co ordinates of start of bus route and bus stop
    arr.append([0.01, 53.45927628199057, -2.2276463370981574])
    arr.append([0.01, 53.4645870298434, -2.2320827813567172])
    return arr

def number_of_cells(point_density_arr, cell_size = CELL_SIZE):
    arr = []
    for i in range(len(point_density_arr) - 1):
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
def start_offset(density_array, point_density, lat_new=53.44537775031849,
                 long_new=-2.2180905798922557, cell_size=CELL_SIZE):
    n_start = int(distance_lat_long(point_density[0][1], point_density[0][2],
                                    lat_new, long_new)/cell_size)
    return density_array[n_start:]

def density_array_linear():
    df_count = clean_count_data()
    point_density_array = point_density(df_count)
    cell_array = number_of_cells(point_density_array)
    density_array = linear_density_gradient(point_density_array, cell_array)
    offset_density_array = start_offset(density_array, point_density_array)
    return density_array, offset_density_array

def main():
    density_array, offset_density_array = density_array_linear()
    print(density_array)
    print(offset_density_array)

if __name__ == "__main__":
    main()