import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session, flash
from modules.feature_extraction import extract_features
from modules.anomaly_detection import AnomalyDetector
from modules.decision_engine import decision_engine
import os
import subprocess
import sys
import json
import threading
import socket

# --- App Initialization ---
app = Flask(__name__)
app.secret_key = os.urandom(24)

# --- Load trained model ---
model_path = "models/ocsvm_model.pkl"
detector = AnomalyDetector()
detector.load(model_path)

# --- In-memory log storage ---
login_logs = []

# --- Helper Function ---
def is_authenticated():
    return session.get('authenticated', False)

# --- Helper to check if port is in use ---
def is_port_in_use(port=8501):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# --- Launch Streamlit in background ---
def run_streamlit():
    if not is_port_in_use(8501):
        try:
            subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Failed to launch Streamlit: {e}")

# Launch Streamlit automatically when main2.py starts
threading.Thread(target=run_streamlit, daemon=True).start()


# -------------------------------
# ROUTE 1: LOGIN
# -------------------------------
@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        fraud_mode = 'fraud_mode' in request.form

        # --- Simulate behavioral session data ---
        if fraud_mode:
            geo_loc, sim_loc = "Delhi", "Mumbai"
            new_device, new_ip, vpn = True, True, True
            failed_logins, geo_distance = 3, 85
            latency_mean, variance = 380, 55
            swipe_speed, swipe_pressure = 1500, 0.35
        else:
            geo_loc, sim_loc = "Mumbai", "Mumbai"
            new_device, new_ip, vpn = False, False, False
            failed_logins, geo_distance = 0, 2
            latency_mean, variance = 210, 35
            swipe_speed, swipe_pressure = 950, 0.65

        latencies_ms = np.random.normal(loc=latency_mean, scale=variance + 1, size=10)
        timestamps_sec = np.cumsum(latencies_ms) / 1000.0

        raw_session = {
            "user_id": username,
            "session_id": "S001",
            "device_id": "DEV_XYZ",
            "ip_address": "198.51.100.23",
            "geo_location": geo_loc,
            "sim_registered_location": sim_loc,
            "keystrokes": [{"timestamp": float(t)} for t in timestamps_sec],
            "swipes": [{"distance": swipe_speed, "duration": 1, "pressure": swipe_pressure} for _ in range(5)],
            "navigation": ["login"],
            "login_hour": 10,
            "new_device": new_device,
            "new_ip": new_ip,
            "vpn": vpn,
            "failed_logins": failed_logins,
            "geo_distance": geo_distance
        }

        # --- Extract features + compute decision ---
        features = extract_features(raw_session)
        confidence = detector.score(features)
        decision = decision_engine(confidence)
        decision_str = decision["decision"].replace("_", " ").strip().lower()

        # --- Log session ---
        login_logs.append({
            "User": username,
            "Decision": decision["decision"],
            "Reason": decision["reason"],
            "Confidence": round(confidence, 2),
            "FraudSimulated": fraud_mode
        })

        if decision_str == "access granted":
            session['authenticated'] = True
            session['username'] = username
            flash(f"Welcome {username}! Access Granted.", 'success')
            return redirect(url_for('bank_dashboard'))
        else:
            session['authenticated'] = False
            flash(f"{decision['decision'].replace('_', ' ').title()}: {decision['reason']}", 'error')
            return redirect(url_for('login'))

    return render_template('login.html', title="Login")


# -------------------------------
# ROUTE 2: BANK DASHBOARD
# -------------------------------
@app.route("/dashboard")
def bank_dashboard():
    if not is_authenticated():
        flash("Please login first to access the dashboard.", 'warning')
        return redirect(url_for('login'))

    tx_data = [
        {"Date": "2025-08-27", "Description": "UPI Transfer to Rahul", "Amount": "-₹2,500"},
        {"Date": "2025-08-25", "Description": "Salary Credit", "Amount": "+₹55,000"},
        {"Date": "2025-08-22", "Description": "Online Purchase", "Amount": "-₹3,200"}
    ]
    return render_template('bank_dashboard.html', title="Bank Dashboard", transactions=tx_data)


# -------------------------------
# ROUTE 3: SOC DASHBOARD
# -------------------------------
@app.route("/soc")
def soc_dashboard():
    if not login_logs:
        return render_template('soc_dashboard.html', title="SOC Dashboard", logs=None)

    log_df = pd.DataFrame(login_logs)
    decision_counts = log_df["Decision"].value_counts()
    fraud_counts = log_df["FraudSimulated"].value_counts()

    return render_template(
        'soc_dashboard.html',
        title="SOC Dashboard",
        logs=log_df.to_dict(orient='records'),
        chart_js=True,
        decision_labels=decision_counts.index.tolist(),
        decision_values=decision_counts.values.tolist(),
        fraud_labels=fraud_counts.index.map(str).tolist(),
        fraud_values=fraud_counts.values.tolist()
    )


# -------------------------------
# ROUTE 4: HOW IT WORKS
# -------------------------------
@app.route("/how_it_works", methods=['GET', 'POST'])
def how_it_works():
    # Redirect to Streamlit for interactive demo
    return redirect("http://localhost:8501")


# -------------------------------
# ROUTE 5: LOGOUT
# -------------------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been successfully logged out.", 'success')
    return redirect(url_for('login'))


# --- Main execution ---
if __name__ == '__main__':
    app.run(debug=True)

