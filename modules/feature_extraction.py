import numpy as np
import pandas as pd
from typing import Dict, Any

def extract_features(raw_session: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts behavioral and contextual features from a raw session event.
    Matches schema in project documentation including engineered features
    required by the trained anomaly detection model.
    """

    # --- Keystroke Dynamics ---
    keystrokes = raw_session.get("keystrokes", [])
    if keystrokes:
        latencies = np.diff([k["timestamp"] for k in keystrokes])
        keystroke_latency_mean = float(np.mean(latencies)) if len(latencies) > 0 else 0.0
        keystroke_variance = float(np.var(latencies)) if len(latencies) > 0 else 0.0
    else:
        keystroke_latency_mean, keystroke_variance = 0.0, 0.0

    # --- Swipe / Touch Biometrics ---
    swipes = raw_session.get("swipes", [])
    if swipes:
        speeds = [s["distance"] / max(s["duration"], 1e-3) for s in swipes]
        pressures = [s.get("pressure", 0.5) for s in swipes]
        swipe_speed_mean = float(np.mean(speeds))
        swipe_pressure_avg = float(np.mean(pressures))
    else:
        swipe_speed_mean, swipe_pressure_avg = 0.0, 0.0

    # --- Navigation Pattern ---
    navigation = raw_session.get("navigation", [])
    navigation_pattern = "→".join(navigation) if navigation else "none"

    # --- Contextual Features ---
    device_change_flag = int(raw_session.get("new_device", False))
    ip_change_flag = int(raw_session.get("new_ip", False))
    vpn_usage_detected = int(raw_session.get("vpn", False))
    failed_login_attempts = int(raw_session.get("failed_logins", 0))

    # --- Location ---
    distance_from_sim_location_km = float(raw_session.get("geo_distance", 0.0))

    # --- Engineered Features ---
    high_speed_and_far_distance = int((swipe_speed_mean > 1200) and (distance_from_sim_location_km > 50))
    new_device_and_failed_logins = int(device_change_flag and (failed_login_attempts > 0))
    vpn_newip = int(vpn_usage_detected and ip_change_flag)

    # --- Meta ---
    user_id = raw_session.get("user_id", "unknown")
    session_id = raw_session.get("session_id", "sess_0")
    device_id = raw_session.get("device_id", "dev_unknown")
    ip_address = raw_session.get("ip_address", "0.0.0.0")
    geo_location = raw_session.get("geo_location", "unknown")
    sim_registered_location = raw_session.get("sim_registered_location", "unknown")
    login_hour = int(raw_session.get("login_hour", 0))

    # Assemble final feature vector
    features = {
        "user_id": user_id,
        "session_id": session_id,
        "device_id": device_id,
        "ip_address": ip_address,
        "geo_location": geo_location,
        "sim_registered_location": sim_registered_location,
        "keystroke_latency_mean": keystroke_latency_mean,
        "keystroke_variance": keystroke_variance,
        "swipe_speed_mean": swipe_speed_mean,
        "swipe_pressure_avg": swipe_pressure_avg,
        "navigation_pattern": navigation_pattern,
        "login_hour": login_hour,
        "device_change_flag": device_change_flag,
        "ip_change_flag": ip_change_flag,
        "distance_from_sim_location_km": distance_from_sim_location_km,
        "vpn_usage_detected": vpn_usage_detected,
        "failed_login_attempts": failed_login_attempts,
        # --- engineered features ---
        "high_speed_and_far_distance": high_speed_and_far_distance,
        "new_device_and_failed_logins": new_device_and_failed_logins,
        "vpn_newip": vpn_newip
    }

    return features


def features_to_dataframe(feature_list: list) -> pd.DataFrame:
    """
    Converts list of feature dicts into a Pandas DataFrame
    for ML training/inference.
    """
    return pd.DataFrame(feature_list)

