siot的Python库
================================================

SIoT是一款开源的MQTT服务器，siot则是Python和MicroPython的一个库。

-------------
简介
-------------

MQTT的库明显不好用，前面要定义一个类，代码还很长，让初学者不知所措。

siot是虚谷物联团队写的一个Python库。为了让初学者能够写出更加简洁、优雅的Python代码。

siot库同时支持MicroPython，语法完全一致。

-------------
安装
-------------

使用pip命令： pip install siot

**注**：虚谷号中已经内置了siot库。

-------------
官方地址
-------------

- GitHub地址：https://github.com/vvlink/SIoT/tree/master/siot-lib

-------------
使用说明
-------------

1.导入库

import siot

2.连接MQTT服务器

siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()
siot.loop()

3.发送消息

siot.publish(IOT_pubTopic, "value %d"%tick)

4.订阅消息

siot.subscribe(IOT_pubTopic, sub_cb)

“sub_cb”为回调函数的名称，需要写一个名称为“sub_cb”的函数，带3个参数，其中msg为订阅的消息，为一个元组，属性有topic和payload。如下面的代码。

::
	def sub_cb(client, userdata, msg):	  print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload))

-------------
代码范例
-------------

1.发送消息：

::

	import siot
	import time

	SERVER = "127.0.0.1"            #MQTT服务器IP
	CLIENT_ID = ""                  #在SIoT上，CLIENT_ID可以留空
	IOT_pubTopic  = 'xzr/001'       #“topic”为“项目名称/设备名称”
	IOT_UserName ='siot'            #用户名
	IOT_PassWord ='dfrobot'         #密码

	siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
	siot.connect()
	siot.loop()

	tick = 0

	try:
	    while True:
	        siot.publish(IOT_pubTopic, "value %d"%tick)
	        time.sleep(1)           #隔1秒发送一次
	        tick = tick+1
	except:
 	   siot.stop()
 	   print("disconnect seccused")

- 订阅消息：

::

	import siot
	import time

	SERVER = "127.0.0.1"        #MQTT服务器IP
	CLIENT_ID = ""              #在SIoT上，CLIENT_ID可以留空
	IOT_pubTopic  = 'xzr/001'   #“topic”为“项目名称/设备名称”
	IOT_UserName ='siot'        #用户名
	IOT_PassWord ='dfrobot'     #密码

	def sub_cb(client, userdata, msg):
	  print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload))

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
