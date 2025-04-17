import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import time
from components.vehicle_status import display_vehicle_status
from components.signal_controls import display_signal_controls
from backend.traffic_predictor import predict_traffic_density

# Load sample vehicle data
vehicles_df = pd.read_csv("data/sample_vehicles.csv")

st.set_page_config(page_title="ResQRoute Dashboard", layout="wide")

st.title("🚨 ResQRoute - Emergency Response Optimizer")

# Sidebar
st.sidebar.header("📊 Dashboard Controls")
selected_vehicle = st.sidebar.selectbox("Select Emergency Vehicle", vehicles_df['vehicle_id'].unique())
current_time = st.sidebar.slider("Select Hour of Day", 0, 23, 10)

# Traffic prediction
traffic_status = predict_traffic_density(current_time)
st.sidebar.markdown(f"### 🚦 Predicted Traffic: `{traffic_status}`")

st.markdown("---")

# Main Panels
col1, col2 = st.columns(2)

with col1:
    display_vehicle_status(selected_vehicle)

with col2:
    display_signal_controls(selected_vehicle)
