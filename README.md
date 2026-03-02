# NBA Injury Risk Prediction

**SIADS 696: Milestone II — Winter 2026**
**University of Michigan, School of Information**

**Team Members:** Ashhad Jaffer, Naseem Heydari, Jeremy Tang

---

## Project Overview

Injuries play a major role in shaping NBA team performance and player careers. This project explores whether player-level statistics, physical attributes, and injury history can predict a player's likelihood of appearing on injury reports in the following season.

We combine publicly available NBA injury transaction records (2013–2018) with official player statistics to build a player-season level dataset. Using this data, we train supervised models to predict next-season injury report counts and apply unsupervised clustering to identify player injury risk archetypes.

### Key Findings

- **Supervised Learning:** XGBoost achieved the best test MAE of 0.941 (10.2% improvement over baseline), but all models only modestly beat the mean-prediction baseline — confirming injury prediction carries inherently weak signal.
- **Unsupervised Learning:** Clustering revealed two broad player archetypes (high-usage starters vs. low-usage role players), but player profiles exist along a continuum rather than discrete risk categories.
- **Most Important Predictor:** Prior injury history — previously injured players are roughly 2x more likely to appear on future injury reports.

---

## Data Sources

| Source | Description | Link |
|--------|-------------|------|
| **elap733/NBA-Injury-Data** | Pre-scraped NBA injury transaction records from Pro Sports Transactions | [GitHub](https://github.com/elap733/NBA-Injury-Data) |
| **nba_api** | Official NBA statistics (box scores, player bio, tracking data, schedules) | [GitHub](https://github.com/swar/nba_api) |
| **Pro Sports Transactions** | Original injury transaction source | [Website](https://www.prosportstransactions.com) |

---

## Repository Structure

```
├── README.md
├── report/
│   └── SIADS696_Final_Report.pdf
├── notebooks/
│   ├── 01_data_collection.ipynb      # API calls & raw data download
│   ├── 02_data_cleaning.ipynb        # Cleaning, filtering, ID matching
│   ├── 03_eda.ipynb                  # Exploratory data analysis
│   ├── 04_feature_engineering.ipynb   # Feature creation & train/test split
│   ├── 05_supervised_models.ipynb     # LR, Random Forest, XGBoost
│   └── 06_unsupervised_models.ipynb   # K-Means & Hierarchical Clustering
├── src/
│   ├── config.py                      # Project constants & paths
│   └── utils.py                       # Helper functions (name matching, etc.)
├── data/
│   ├── raw/                           # Raw downloaded files (not tracked)
│   │   ├── elap733/                   # Injury CSV files by season
│   │   └── nba_api/                   # Stats, bio, tracking, schedule CSVs
│   └── processed/                     # Cleaned & model-ready files
│       ├── train.csv                  # Training set (1,620 rows × 16 cols)
│       └── test.csv                   # Test set (412 rows × 16 cols)
└── requirements.txt
```

---

## Pipeline Overview

The project follows a six-notebook pipeline, each building on the previous:

| Notebook | Purpose | Output |
|----------|---------|--------|
| **NB01** | Download injury data + NBA stats via API | 28 raw CSV files |
| **NB02** | Clean, filter, merge, fuzzy match player IDs | 7 processed CSVs |
| **NB03** | EDA — distributions, correlations, injury patterns | `analysis_merged.csv` |
| **NB04** | Engineer features, shift target, train/test split | `train.csv`, `test.csv` |
| **NB05** | Train 3 supervised model families, evaluate | Best model: XGBoost (MAE 0.941) |
| **NB06** | K-Means + Hierarchical clustering | 2 player archetypes identified |

---

## Features

15 engineered features across 5 categories:

| Category | Features |
|----------|----------|
| Workload (5) | `min`, `gp`, `dist_miles`, `usg_pct`, `ts_pct` |
| Physical (3) | `age`, `player_height_inches`, `player_weight` |
| Injury History (2) | `injured_last_season`, `injury_report_count_last_season` |
| Team Context (1) | `b2b_games` |
| Interactions (4) | `age_x_minutes`, `weight_x_minutes`, `b2b_x_minutes`, `age_x_weight` |

**Target:** `target_next_season` — injury report appearances in the following season.

---

## Supervised Learning Results

| Model | CV MAE (mean ± std) | Test MAE | Test RMSE | Test R² |
|-------|---------------------|----------|-----------|---------|
| Baseline (Mean) | N/A | 1.048 | 1.250 | -0.032 |
| Linear Regression | 1.158 ± 0.109 | 0.928 | 1.172 | 0.093 |
| Random Forest (tuned) | 1.142 ± 0.109 | 0.964 | 1.211 | 0.033 |
| **XGBoost (tuned)** | **1.130 ± 0.113** | **0.941** | **1.189** | **0.067** |

---

## Setup & Reproducibility

### Requirements

```
pandas
numpy
scikit-learn
xgboost
matplotlib
nba_api
fuzzywuzzy
python-Levenshtein
```

### Running the Pipeline

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run notebooks in order: `01` → `02` → `03` → `04` → `05` → `06`
4. NB01 downloads raw data via API (requires internet). Subsequent notebooks use saved CSVs.

> **Note:** NBA API calls include rate limiting (`time.sleep`) and skip-if-exists logic. Initial data collection may take 15–20 minutes.

---

## References

1. Cohan, A., Schuster, J., & Fernandez, J. (2021). A deep learning approach to injury forecasting in NBA basketball. *Journal of Sports Analytics*, 7(3), 177–190.
2. Haeberle, H. S., et al. (2022). Machine Learning for Predicting Lower Extremity Muscle Strain in NBA Athletes. *Orthopaedic Journal of Sports Medicine*, 10(7).
3. Karypidis, E., et al. (2024). Unsupervised Learning in NBA Injury Recovery. *Information*, 15(1), 61.
4. swar/nba_api — https://github.com/swar/nba_api
5. elap733/NBA-Injury-Data — https://github.com/elap733/NBA-Injury-Data