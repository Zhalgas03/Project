import time
import json
import paho.mqtt.client as mqtt
from neo4j import GraphDatabase
import sys
sys.path.append('../python')
from settings import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
from utils import generate_sensor_data, setup_mqtt_client

# Initialize Neo4j driver
neo4j_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")
    
    # Save the message to Neo4j
    with neo4j_driver.session() as session:
        session.run(
            "CREATE (s:SensorData {topic: $topic, message: $message})",
            topic=msg.topic,
            message=message
        )
    print("Message saved to Neo4j")

# Initialize the MQTT client
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

    neo4j_driver.close()
    print("Neo4j connection closed")
