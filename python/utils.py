import random
import json
import paho.mqtt.client as mqtt
from settings import MQTT_BROKER, MQTT_PORT

def generate_sensor_data():
    air_quality = round(random.uniform(0, 100), 2)
    temperature = round(random.uniform(-20, 40), 2)
    humidity = round(random.uniform(0, 100), 2)
    
    sensor_data = {
        "air_quality": air_quality,
        "temperature": temperature,
        "humidity": humidity
    }
    
    return sensor_data

def setup_mqtt_client(client, topic, on_message):
    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT broker")
            client.subscribe(topic)
        else:
            print(f"Failed to connect to MQTT broker with code {rc}")

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
