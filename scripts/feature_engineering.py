import pandas as pd

def add_features(df):
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    return df
