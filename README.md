## Analytics Engineering App

This project demonstrates skills aligned with an Analytics Engineering role:

- ETL Pipeline Development
- Data Modeling
- Machine Learning
- Data Visualization
- Business Reporting

        analytics_app_project/
        │
        ├── data/
        │   ├── sales_data.csv
        │   └── customer_data.csv
        │
        ├── scripts/
        │   ├── data_cleaning.py
        │   ├── feature_engineering.py
        │   ├── model_training.py
        │   └── pipeline.py
        │
        ├── utils/
        │   ├── helpers.py
        │   └── config.py
        │
        ├── notebooks/
        │   └── exploratory_analysis.ipynb
        │
        ├── visualizations/
        │   └── dashboard_plot.py
        │
        ├── README.md
        ├── requirements.txt
        └── .gitignore



## Folder Structure

- `data/` - Contains raw CSVs
- `scripts/` - Data pipeline scripts
- `utils/` - Configs and helpers
- `visualizations/` - Dashboard plotting
- `notebooks/` - EDA notebooks

## Quick Start

### Install requirements:

    pip install -r requirements.txt

### Then run the pipeline:

    python scripts/pipeline.py

## Outcome

**Trains** a basic ML model **on** sales data and prepares visualizations.

