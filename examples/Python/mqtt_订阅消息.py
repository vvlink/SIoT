# 订阅消息
# coding=utf-8

import threading
import paho.mqtt.client as mqtt
import time


SERVER = "192.168.0.129"
CLIENT_ID = ""
TOPIC_SUB = 'home/temp'
TOPIC_PUB = 'home/command'
username='siot'
password='dfrobot'
LIMITHIGH = 40
LIMITLOW = 10

client = mqtt.Client(CLIENT_ID)

def _on_connect(myclient,userdata,flags,rc):
    print("Connected with result code " + str(rc))
    myclient.subscribe(TOPIC_SUB)

def _on_message(myclient, userdata, msg):
    print("Topic:" + str(msg.topic) + " Message:" + str(msg.payload))
    if int(msg.payload)<LIMITLOW or int(msg.payload)>LIMITHIGH:
        myclient.publish(TOPIC_PUB,"1")

def loop(timeout=None):
    thread = threading.Thread(target=_loop, args=(timeout,))
    thread.start()

def _loop(timeout=None):
    global client
    if not timeout:
        client.loop_forever()
    else:
        client.loop(timeout)

client.on_connect = _on_connect
client.on_message = _on_message

client.username_pw_set(username,password)
client.connect(SERVER,1883,60)

time.sleep(1)
loop()

while True:
    time.sleep(1)

