from scripts.data_cleaning import clean_sales_data
from scripts.feature_engineering import add_features
from scripts.model_training import train_model

def run_pipeline():
    df = clean_sales_data('data/sales_data.csv')
    df = add_features(df)
    X = df[['Month']]
    y = df['Sales']
    model = train_model(X, y)
    print("Model trained successfully.")

if __name__ == "__main__":
    run_pipeline()
