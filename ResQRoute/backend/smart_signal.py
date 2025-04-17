# smart_signal.py

def override_signal(signal_id, status):
    print(f"Signal {signal_id} changed to {status.upper()}")
    return True
