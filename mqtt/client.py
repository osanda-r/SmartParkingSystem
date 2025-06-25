# MQTT client code
import paho.mqtt.client as mqtt
import json

class MQTTClient:
    def __init__(self, system, broker='broker.hivemq.com', port=1883):
        self.client = mqtt.Client()
        self.system = system
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker, port)

    def start(self):
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("[MQTT] Connected")
        self.client.subscribe("parking/+/occupancy")

    def on_message(self, client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            self.system.process_sensor_data(
                spot_id=data['spot_id'],
                occupied=data['occupied'],
                vehicle_id=data.get('vehicle_id')
            )
        except Exception as e:
            print(f"[ERROR] MQTT message failed: {e}")
