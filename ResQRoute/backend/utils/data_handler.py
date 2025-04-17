import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

def load_vehicle_data():
    return pd.read_csv(os.path.join(DATA_DIR, 'sample_vehicles.csv'))

def load_traffic_data():
    return pd.read_csv(os.path.join(DATA_DIR, 'traffic_data.csv'))

def load_signal_config():
    return pd.read_csv(os.path.join(DATA_DIR, 'signal_config.csv'))

def save_vehicle_data(df):
    df.to_csv(os.path.join(DATA_DIR, 'sample_vehicles.csv'), index=False)

def save_signal_config(df):
    df.to_csv(os.path.join(DATA_DIR, 'signal_config.csv'), index=False)
