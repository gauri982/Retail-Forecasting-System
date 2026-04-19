import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", end="2024-12-31")

products = ["Product_A", "Product_B", "Product_C"]
stores = ["Store_1", "Store_2"]

data = []

for store in stores:
    for product in products:
        base = np.random.randint(20, 50)

        for date in dates:

            seasonal = 15 if date.month in [10,11,12] else 0
            weekend = 5 if date.weekday() >= 5 else 0
            noise = np.random.normal(0, 3)

            sales = max(0, base + seasonal + weekend + noise)
            price = np.random.uniform(100, 500)

            data.append([date, store, product, int(sales), round(price,2)])

df = pd.DataFrame(data, columns=["date","store","product","sales","price"])

df.to_csv("data/raw/sales_data.csv", index=False)

print("Dataset created successfully!")