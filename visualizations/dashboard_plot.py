import pandas as pd
import matplotlib.pyplot as plt

def plot_sales(filepath):
    df = pd.read_csv(filepath)
    plt.plot(df['Date'], df['Sales'])
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
