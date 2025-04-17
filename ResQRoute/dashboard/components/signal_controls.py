import streamlit as st
import pandas as pd
import os
import sys

# Ensure access to backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend.smart_signal import override_signal

def display_signal_controls(signal_id):
    st.subheader(f"🚦 Signal Control: {signal_id}")

    status = st.radio("Select Signal Status", ('Green', 'Red', 'Yellow'))

    if st.button("Override Signal"):
        override_signal(signal_id, status)
        st.success(f"✅ Signal {signal_id} overridden to {status}")
