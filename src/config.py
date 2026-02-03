"""Project configuration and constants."""

# Season range
FIRST_SEASON = 2010
LAST_SEASON = 2019

# Train/test split
TRAIN_SEASONS = list(range(2010, 2018))  # 2010-2017
TEST_SEASONS = [2018, 2019]

# Tracking data availability (NBA.com tracking starts 2013-14)
TRACKING_DATA_START = 2013

# Data paths
RAW_ELAP_DIR = "data/raw/elap733"
RAW_NBA_API_DIR = "data/raw/nba_api"
PROCESSED_DIR = "data/processed"
FINAL_DIR = "data/final"

# Target variable
TARGET_COL = "games_missed_next_season"

# Random seed for reproducibility
RANDOM_SEED = 42
