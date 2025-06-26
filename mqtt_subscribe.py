import paho.mqtt.client as mqtt
from random import randint, getrandbits
import time

class Smartphone:
    def __init__(self):
        self.broker = 'mqtt.eclipseprojects.io'
        self.client = mqtt.Client()
        self.client.connect(self.broker)


def on_message(client, userdata, message):
    print(f"Received Mesage: \n{str(message.payload)}")
    
    
s = Smartphone()
while True:
    s.client.loop_start()
    s.client.subscribe("TELEMETRYspc")
    s.client.on_message = on_message
    time.sleep(30)

s.client.loop_stop()
    
    