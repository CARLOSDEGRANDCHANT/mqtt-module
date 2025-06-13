import paho.mqtt.client as mqtt
from random import randint
import time


mqttBroker = 'mqtt.eclipseprojects.io'
client = mqtt.Client()
client.connect(mqttBroker)

while True:
    randomNumber = randint(1, 200)
    client.publish("POS", randomNumber)
    print(f"Published 'TEMPERATURE': {randomNumber}")
    time.sleep(10)