import pandas as pd

def clean_sales_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    return df
