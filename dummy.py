import paho.mqtt.client as mqtt
import json
import random
import time
from dotenv import load_dotenv
import os
load_dotenv()
MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
# MQTT_USERNAME = os.getenv("MQTT_USERNAME")
# MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
MQTT_TOPIC = os.getenv("MQTT_TOPIC")

# Fungsi callback untuk koneksi
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to broker")
    else:
        print(f"Connect failed with code {rc}")

# Membuat klien MQTT
client = mqtt.Client()

# Mengatur callback untuk koneksi
client.on_connect = on_connect

# Menghubungkan ke broker MQTT
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Memulai loop untuk memproses callback
client.loop_start()

try:
    while True:
        # Membuat data acak
        data = {
            "temperature": random.randint(0, 100),
            "humidity": random.randint(0, 100),
            "ammonia": random.randint(0, 100)
        }
        
        # Mengubah data menjadi JSON string
        payload = json.dumps(data)
        
        # Mengirim pesan ke topik
        result = client.publish(MQTT_TOPIC, payload)
        
        # Memeriksa apakah pengiriman pesan berhasil
        status = result[0]
        if status == 0:
            print(f"Sent `{payload}` to topic `{MQTT_TOPIC}`")
        else:
            print(f"Failed to send message to topic {MQTT_TOPIC}")
        
        # Menunggu selama 5 detik sebelum mengirim data lagi
        time.sleep(1)

except KeyboardInterrupt:
    print("Terminating the program")

finally:
    # Memberikan waktu untuk menyelesaikan pengiriman pesan terakhir
    client.loop_stop()
    client.disconnect()
