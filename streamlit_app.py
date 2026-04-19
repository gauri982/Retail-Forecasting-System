import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from prophet import Prophet

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Retail Forecasting Dashboard", layout="wide")

st.title("📊 Retail Sales Forecasting & Inventory Dashboard")

# -----------------------------
# SAFE PATH HANDLING (FIX)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "sales_data.csv")

# Load dataset safely
df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

product = st.sidebar.selectbox("Select Product", df['product'].unique())
store = st.sidebar.selectbox("Select Store", df['store'].unique())

filtered_df = df[(df['product'] == product) & (df['store'] == store)]

# -----------------------------
# DAILY SALES
# -----------------------------
daily_sales = filtered_df.groupby('date')['sales'].sum()

st.subheader("📈 Sales Trend")
st.line_chart(daily_sales)

# -----------------------------
# FORECASTING MODEL
# -----------------------------
st.subheader("🔮 30-Day Forecast")

forecast_df = daily_sales.reset_index()
forecast_df.columns = ['ds', 'y']

model = Prophet()
model.fit(forecast_df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

fig1 = model.plot(forecast)
st.pyplot(fig1)

# -----------------------------
# INVENTORY OPTIMIZATION
# -----------------------------
st.subheader("📦 Inventory Optimization")

avg_demand = daily_sales.mean()
std_demand = daily_sales.std()

lead_time = 7
z = 1.65  # 95% service level

safety_stock = z * std_demand * (lead_time ** 0.5)
reorder_point = (avg_demand * lead_time) + safety_stock

st.write("📊 Average Demand:", round(avg_demand, 2))
st.write("🛡 Safety Stock:", round(safety_stock, 2))
st.write("🚨 Reorder Point:", round(reorder_point, 2))

current_stock = st.number_input("Enter Current Stock", value=500)

if current_stock <= reorder_point:
    st.error("⚠️ REORDER REQUIRED")
else:
    st.success("✅ STOCK SUFFICIENT")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("Built for Retail Forecasting & Inventory Optimization System 🚀")