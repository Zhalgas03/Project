import time
import json
import paho.mqtt.client as mqtt
import mysql.connector
from settings import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_TABLE
from utils import generate_sensor_data, setup_mqtt_client

# Initialize MySQL connection
try:
    mysql_conn = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    mysql_cursor = mysql_conn.cursor()
    print("Connected to MySQL database")

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {MYSQL_TABLE} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        topic VARCHAR(255) NOT NULL,
        message TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    mysql_cursor.execute(create_table_query)
    print(f"Table '{MYSQL_TABLE}' created successfully")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    exit(1)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")
    
    insert_query = f"INSERT INTO {MYSQL_TABLE} (topic, message) VALUES (%s, %s)"
    insert_values = (msg.topic, message)
    
    try:
        mysql_cursor.execute(insert_query, insert_values)
        mysql_conn.commit()
        print("Message saved to MySQL")
    
    except mysql.connector.Error as err:
        print(f"Error inserting into MySQL: {err}")

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

    if mysql_conn.is_connected():
        mysql_cursor.close()
        mysql_conn.close()
        print("MySQL connection closed")
