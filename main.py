from dotenv import load_dotenv
import os
load_dotenv()
import paho.mqtt.client as mqtt
import asyncio
import multiprocessing
import json

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = os.getenv("MQTT_PORT")
# MQTT_USERNAME = os.getenv("MQTT_USERNAME")
# MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
MQTT_TOPIC = os.getenv("MQTT_TOPIC")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.publish("AIS","Launched...!!!")  # Subscribe ke topik "topic/test"
        client.subscribe(MQTT_TOPIC)  # Subscribe ke topik "topic/test"
    else:
        print("Connection failed")
        
# Fungsi yang dipanggil ketika pesan diterima
def on_message(client, userdata, msg):
    print("Received message on topic:", msg.topic)
    try:
        # Mencoba untuk menguraikan payload sebagai JSON
        payload_json = json.loads(msg.payload)
        # Mencetak payload JSON dengan format yang lebih rapi
        print("Received JSON payload:")
        print(json.dumps(payload_json, indent=4, sort_keys=True))
    except ValueError:
        # Jika payload tidak bisa diuraikan sebagai JSON, cetak sebagai string biasa
        print("Received String Payload:", msg.payload)
        
def mqtt_process():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, 1883, 60)
    client.loop_forever()
    
if __name__ == "__main__":
    mqtt_main = multiprocessing.Process(target=mqtt_process)
    mqtt_main.start() 