import streamlit as st
import pandas as pd

# Title
st.title("📊 ResQRoute Dashboard - Data View")

# Read CSV files
vehicles_df = pd.read_csv("C:/ResQRoute/dashboard/data/sample_vehicles.csv")
traffic_df = pd.read_csv("C:/ResQRoute/dashboard/data/traffic_data.csv")
signals_df = pd.read_csv("C:/ResQRoute/dashboard/data/signal_config.csv")

# Display data
st.header("🚑 Emergency Vehicles")
st.dataframe(vehicles_df)

st.header("🚦 Signal Configurations")
st.dataframe(signals_df)

st.header("🛣️ Traffic Density")
st.dataframe(traffic_df)
