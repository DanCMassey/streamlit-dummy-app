
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Dummy Data Dashboard")

# Generate dummy data
np.random.seed(42)
data = {
    "Date": pd.date_range(start="2024-01-01", periods=100),
    "Sales": np.random.randint(100, 500, size=100),
    "Profit": np.random.normal(loc=50, scale=15, size=100),
    "Region": np.random.choice(["North", "South", "East", "West"], size=100)
}

df = pd.DataFrame(data)

# Show raw data
st.subheader("📊 Raw Dummy Data")
st.dataframe(df.head())

# Summary statistics
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# Filter by region
region = st.selectbox("Select a region to filter", options=df["Region"].unique())
filtered_df = df[df["Region"] == region]

# Line chart
st.subheader(f"📉 Sales Over Time ({region} Region)")
st.line_chart(filtered_df.set_index("Date")["Sales"])

# Histogram
st.subheader("💰 Profit Distribution")
fig, ax = plt.subplots()
ax.hist(df["Profit"], bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig)
