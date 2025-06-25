# Entry point for Smart Parking System
from mqtt.client import MQTTClient
from db.database import DatabaseManager
from auth.auth import AuthManager
from payment.gateway import PaymentGateway
import time

class SmartParkingSystem:
    def __init__(self):
        self.db = DatabaseManager()
        self.auth = AuthManager()
        self.mqtt = MQTTClient(self)
        self.payment = PaymentGateway()

    def process_sensor_data(self, spot_id, occupied, vehicle_id=None):
        print(f"[INFO] Processing: {spot_id}, Occupied={occupied}")
        if occupied:
            self.db.occupy_spot(spot_id, vehicle_id or "GUEST")
        else:
            self.db.vacate_spot(spot_id)

    def handle_payment(self, spot_id, duration):
        amount = self.payment.calculate_fee(duration)
        return self.payment.process_payment(amount, spot_id)

if __name__ == "__main__":
    system = SmartParkingSystem()
    system.mqtt.start()
