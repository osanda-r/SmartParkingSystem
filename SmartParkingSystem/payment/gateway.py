# Simulated payment gateway
class PaymentGateway:
    def calculate_fee(self, duration_minutes):
        rate = 1.0  # 1 currency unit per 15 minutes
        return round((duration_minutes / 15) * rate, 2)

    def process_payment(self, amount, spot_id):
        print(f"[PAYMENT] {amount} processed for spot {spot_id}")
        return True
