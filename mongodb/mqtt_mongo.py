import time
import json
import paho.mqtt.client as mqtt
from pymongo import MongoClient
import sys
sys.path.append('../python')
from settings import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MONGO_URI, MONGO_DB, MONGO_COLLECTION
from utils import generate_sensor_data, setup_mqtt_client

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")
    
    message_document = {
        "topic": msg.topic,
        "message": message
    }
    collection.insert_one(message_document)
    print("Message saved to MongoDB")

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
setup_mqtt_client(mqtt_client, MQTT_TOPIC, on_message)

try:
    while True:
        sensor_data = generate_sensor_data()
        message = json.dumps(sensor_data)
        mqtt_client.publish(MQTT_TOPIC, message)
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("MQTT connection closed")

    mongo_client.close()
    print("MongoDB connection closed")
