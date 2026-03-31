import pandas as pd
from pygments.lexers import q

from .config import RAW_COUNT_DATA, HOUR, DIRECTIONS, COUNT_POINT_IDS


def clean_count_data(data_file = RAW_COUNT_DATA, count_point_id = COUNT_POINT_IDS,direction = DIRECTIONS):
    df_count = pd.read_csv(data_file, low_memory=False)
    df_count = df_count.drop(columns=[
        'region_id', 'region_name', 'local_authority_id', 'local_authority_name',
        'easting', 'northing', 'pedal_cycles', 'two_wheeled_motor_vehicles', 'cars_and_taxis',
        'hgvs_2_rigid_axle', 'hgvs_3_rigid_axle', 'hgvs_4_or_more_rigid_axle',
        'hgvs_3_or_4_articulated_axle', 'hgvs_5_articulated_axle', 'hgvs_6_articulated_axle',
        'lgvs', 'all_hgvs', 'link_length_miles', 'link_length_km', 'start_junction_road_name', 'end_junction_road_name',
        'road_type', 'count_date'
    ])
    df_count = df_count[df_count['count_point_id'].isin(count_point_id)]
    df_count = df_count[df_count['year'].between(2008, 2016)]
    df_count = df_count[df_count['direction_of_travel'].isin(direction)]
    df_count = df_count[df_count['hour'].isin(HOUR)]
    return df_count