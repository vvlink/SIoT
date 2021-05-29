
'''
# file siot.py

# brief         download into pc or raspberryPi and run the demo
# Copyright     Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
# licence       The MIT License (MIT)
# author        [LuoYufeng](yufeng.luo@dfrobot.com)
# version       V1.0
# date          2019-10-8
'''

name = "DFRobot_siot"

__all__ = ['init', 'connect', 'publish', 'subscribe', '_on_connect', 'set_callback', 'getsubscribe', 'stop', 'publloopish', '_loop']

import threading
import paho.mqtt.client as mqtt
import time

timer = None

def init(client_id, server, port=1883, user=None, password=None):
    global _host, _port, _user, _password, client
    _host = server
    _port = port
    _user = user
    _password = password
    client = mqtt.Client(client_id)
    client.on_connect = _on_connect

def connect():
    client.username_pw_set(_user, _password)
    client.connect(_host, _port, 60)

def publish(topic, data):
    client.publish(str(topic), str(data))
  
def subscribe(topic, cb):
    client.on_message  = cb
    client.subscribe(topic)

def _on_connect(client, userdata, flags, rc):
    if str(rc)=="0":
        print("\n连接结果: 连接成功 ")
    elif str(rc)=="1":
        print("\n连接结果: 协议版本错误 ")
    elif str(rc)=="2":
        print("\n连接结果: 无效的客户端标识 ")
    elif str(rc)=="3":
        print("\n连接结果: 服务器无法使用 ")
    elif str(rc)=="4":
        print("\n连接结果: 错误的用户名或密码 ")
    else:
        print("\n连接结果: 未经授权 ") 
def set_callback(cb):
    client.on_message = cb

def getsubscribe(topic):
    client.subscribe(topic)

def stop():
    client.disconnect()
    if timer != None:
        timer.cancel()
 
def loop(timeout=None):
    thread = threading.Thread(target=_loop, args=(timeout,))
    # thread.setDaemon(True)
    thread.start()
    
def _loop(timeout=None):
    if not timeout:
        client.loop_forever()
    else:
        client.loop(timeout)
