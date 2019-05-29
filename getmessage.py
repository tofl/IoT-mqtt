import paho.mqtt.client as mqtt

host = "192.168.99.100"
port = 1883

client = mqtt.Client()
client.connect(host, port)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("test")

def get_message(client, userdata, msg):
    print(msg.payload.decode())

client.on_message = get_message
client.on_connect = on_connect

client.loop_forever()