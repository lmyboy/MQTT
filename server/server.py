import paho.mqtt.client as mqtt
import datetime

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("IoT-Now/#")

def on_message(client, userdata, msg):
    print(str(datetime.datetime.now()) + ": " + msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.lucascavalcanti.com", 1883, 60)

client.loop_forever()