# NBA Player Injury Risk Prediction

**Team Members:** Ashhad, Jeremy, Naseem
**Course:** SIADS 696 Milestone 2, University of Michigan Master of Applied Data Science

## Problem Description

This project predicts how many games an NBA player will miss due to injury in the following season using supervised learning (regression) and clusters players into injury risk archetypes using unsupervised learning.

## Data Sources

1. **[elap733/NBA-Injuries-Analysis](https://github.com/elap733/NBA-Injuries-Analysis)**
   Pre-scraped injury transaction data from prosportstransactions.com (2010-2019). Provides injury records and games missed calculations.

2. **[nba_api](https://github.com/swar/nba_api)**
   Official NBA.com stats API wrapper. Used for player statistics, biographical data, tracking data (2013-14+), and team schedules.

## Repository Structure

```
SIADS-696-NBA-INJURY-PREDICTION/
├── data/
│   ├── raw/
│   │   ├── elap733/          # Injury CSV files from elap733 repo
│   │   └── nba_api/          # Player stats, tracking data, schedules
│   ├── processed/            # Cleaned and merged datasets
│   └── final/                # Model-ready datasets
├── figures/                  # Visualizations and plots
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_supervised_models.ipynb
│   ├── 06_unsupervised_models.ipynb
│   └── 07_results_analysis.ipynb
├── reports/                  # Final reports and documentation
├── src/
│   ├── config.py             # Project constants and configuration
│   └── utils.py              # Utility functions
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Data Setup

1. Clone the [elap733/NBA-Injuries-Analysis](https://github.com/elap733/NBA-Injuries-Analysis) repository and copy the relevant CSV files to `data/raw/elap733/`
2. Run `notebooks/01_data_collection.ipynb` to pull player data from nba_api
