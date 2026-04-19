from src.data_loader import load_data
from src.preprocessing import clean_data

# Load data
df = load_data("data/raw/sales_data.csv")

print("\nRAW DATA SAMPLE:")
print(df.head())

# Clean data
df_clean = clean_data(df)

print("\nCLEANED DATA SAMPLE:")
print(df_clean.head())