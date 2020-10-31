#!/usr/bin/python3
import paho.mqtt.client as mqtt
import time
from threading import Thread

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with MQTT Broker")
    else:
        print("Connection Failed!")

def on_message(client, userdata, msg):
    print("{} :: {}".format(msg.topic, msg.payload))

def Run(input1, input2, input3):

    HOST_NAME = input1
    HOST_PORT = int(input2)
    TOPIC = input3

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(HOST_NAME, HOST_PORT)
    client.loop_start()

    client.subscribe(TOPIC)

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Saindo...")
        client.disconnect()
        client.loop_stop()
