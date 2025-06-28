
import paho.mqtt.client as mqtt
import json
import time
import random

broker = 'broker.hivemq.com'
port = 1883
topic = 'parking/zoneA/occupancy'
spot_ids = ['A-001', 'A-002', 'A-003']

client = mqtt.Client()
client.connect(broker, port)

def simulate_occupancy():
    while True:
        spot_id = random.choice(spot_ids)
        occupied = random.choice([True, False])
        vehicle_id = f"VHI-{random.randint(1000, 9999)}" if occupied else None

        payload = {
            "spot_id": spot_id,
            "is_occupied": occupied,
            "vehicle_id": vehicle_id
        }

        client.publish(topic, json.dumps(payload))
        print(f"Sent -> {payload}")
        time.sleep(5)  # simulate every 5 seconds

if __name__ == "__main__":
    simulate_occupancy()
