from flask import Flask, request, jsonify
from db.database import DatabaseManager
from payment.gateway import PaymentGateway
from datetime import datetime
import random

app = Flask(__name__)
db = DatabaseManager()
gateway = PaymentGateway()

# Simulated memory cache (entry time per vehicle)
spot_times = {}

@app.route("/status", methods=["GET"])
def get_all_spots():
    return jsonify(db.get_all_spots())

@app.route("/gate/<spot_id>", methods=["POST"])
def control_gate(spot_id):
    # Simulated gate action
    return f"Gate toggled for {spot_id}", 200

@app.route("/emergency-exit", methods=["POST"])
def emergency_exit():
    db.vacate_all_spots()
    return "Emergency exit triggered – all spots vacated.", 200

@app.route("/payment/<spot_id>", methods=["POST"])
def handle_payment(spot_id):
    # Simulate entry time tracking
    start_time = spot_times.get(spot_id, datetime.now())
    duration = random.randint(5, 120)  # Simulated stay in minutes
    amount = gateway.calculate_fee(duration)
    db.vacate_spot(spot_id)

    return jsonify({
        "spot": spot_id,
        "duration": duration,
        "amount": amount
    })

@app.route("/camera/<spot_id>", methods=["POST"])
def camera_control(spot_id):
    return f"Camera triggered at {spot_id}", 200

if __name__ == "__main__":
    app.run(debug=True)
