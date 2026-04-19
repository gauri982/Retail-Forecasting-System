import pandas as pd

def clean_data(df):
    """
    Clean retail sales dataset
    """

    # 1. Check missing values
    print("Missing values:\n", df.isnull().sum())

    # 2. Fill missing values (if any)
    df['sales'] = df['sales'].fillna(df['sales'].median())
    df['price'] = df['price'].fillna(df['price'].median())

    # 3. Remove duplicates
    df = df.drop_duplicates()

    # 4. Convert date if not already
    df['date'] = pd.to_datetime(df['date'])

    # 5. Feature engineering (basic time features)
    df['day_of_week'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    # 6. Sort for time-series modeling
    df = df.sort_values(by='date')

    return df