import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date')
    return df