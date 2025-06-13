import paho.mqtt.client as mqtt
from random import randint
import time



class Engine:
    def __init__(self):
        self.mqttBroker = 'mqtt.eclipseprojects.io'
        self.client = mqtt.Client()
        self.client.connect(self.mqttBroker)

    def run(self):
        while True:
            randomNumber = randint(1, 200)
            self.client.publish("TEMPERATUREspc", randomNumber)
            print(f"Published 'TEMPERATURE': {randomNumber}")
            time.sleep(10)
            
e = Engine()
e.run()