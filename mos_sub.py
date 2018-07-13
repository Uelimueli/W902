import subprocess
from subprocess import call
import paho.mqtt.client as mqtt
import os
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("test")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "1":
    os.system("/home/pi/cam.py")
    client.disconnect()

client = mqtt.Client()
client.connect("10.71.56.173",1883,60)

client.on_connect = on_connect
