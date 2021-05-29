'''
# file sub.py

# brief         Set 'SERVER','CLIENT_ID'(this can be null),'IOT_pubTopic','IOT_UserName','IOT_PassWord'
#               download into pc or raspberryPi and run the file
#               You receive the message from server
# Copyright     Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
# licence       The MIT License (MIT)
# author        [LuoYufeng](yufeng.luo@dfrobot.com)
# version       V1.0
# date          2019-10-8
'''

import siot
import time

SERVER = "127.0.0.1"        #MQTT服务器IP
CLIENT_ID = ""              #在SIoT上，CLIENT_ID可以留空
IOT_pubTopic  = 'xzr/001'   #“topic”为“项目名称/设备名称”
IOT_UserName ='siot'        #用户名
IOT_PassWord ='dfrobot'     #密码

def sub_cb(client, userdata, msg):
  print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload))
  # msg.payload中是消息的内容，类型是bytes，需要用解码。
  s=msg.payload.decode()
  print(s)


siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()
siot.subscribe(IOT_pubTopic, sub_cb)
siot.loop()

try:
  while True:
    pass
except:
  siot.stop()
  print("disconnect seccused")
