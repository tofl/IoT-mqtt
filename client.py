import paho.mqtt.client as mqtt
import threading
import random

host = "192.168.99.100"
port = 1883

# Connexion
client = mqtt.Client("TomFlitterman")
client.connect(host, port)

# Publier des messages :
def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def envoyerMessage():
    randInt = random.randint(1, 50)
    client.publish("test", randInt, 0, False)

setInterval(envoyerMessage, 2)
#client.publish(topic="test", payload="Hello world", qos=0, retain=False)