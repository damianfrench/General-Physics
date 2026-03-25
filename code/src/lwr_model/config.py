from pathlib import Path

# Project root
ROOT = Path(__file__).parents[2]  # goes up: lwr_model/ -> src/ -> code/

# Data
RAW_COUNT_DATA = ROOT / "data" / "raw" / "dft_rawcount_local_authority_id_85.csv"

NAPTAN_URL = "https://naptan.api.dft.gov.uk/v1/access-nodes?atcoAreaCodes=180&dataFormat=csv"
NAPTAN_CODES = ['MANADWGW','MANADWGM','MANADWGD', 'MANADWDP',
                'MANGTMJT', 'MANGTMJP', 'MANGTMJG', 'MANGTMJA']
# Count points
COUNT_POINT_IDS = [944405, 57603, 944412]

# Filter parameters
DIRECTIONS = ["N", "E"]
HOUR = [8]

# Traffic parameters
FREE_SPEEDS = {
    944405: 48,  # km/h
    57603:  48,
    944412: 30,
}

# Model parameters
CELL_SIZE = 10 # in m
