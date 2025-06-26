import paho.mqtt.client as mqtt
from random import randint
import json
import time

class Telemetry:
    def __init__(self, battery, position):
        
        # Inherited attriibutes
        self.battery = battery
        self.position = position
        
        # Attributes for server
        self.mqttBroker = 'mqtt.eclipseprojects.io'
        self.client = mqtt.Client()
        self.client.connect(self.mqttBroker)
        
    def sendMessage(self):
        return self.client.publish("TELEMETRYspc",
             payload=json.dumps({
                'time': time.ctime(),
               'battery': self.battery,
                'position': self.position,
            }))
        
    def getBattery(self):
        self.battery = randint(0, 100)
        
    def getPos(self):
        self.position = randint(0, 100)
        
                  
tel = Telemetry(10, 10)

while True:
    tel.getPos()
    tel.getBattery()
    tel.sendMessage()
    print("Message sent.")
    time.sleep(20)