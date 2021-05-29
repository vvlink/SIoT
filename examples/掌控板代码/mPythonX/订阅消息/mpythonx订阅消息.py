from mpython import *
import network
from umqtt.simple import MQTTClient
from machine import Timer
import ubinascii

my_wifi = wifi()
my_wifi.connectWiFi("makerspace", "m@kersp@ce")

mqtt = MQTTClient("zhangkongban", "192.168.1.135", 1883, "siot", "dfrobot", keepalive=30)

try:
    mqtt.connect()
    print('Connected')
except:
    print('Disconnected')

def mqtt_topic_6d707974686f6e2f303031(_msg):
    oled.fill_rect(0, 0, 128, 16, 0)
    oled.DispChar((str(_msg)), 0, 0, 1)
    oled.show()

def mqtt_callback(topic, msg):
    try:
        topic = topic.decode('utf-8', 'ignore')
        _msg = msg.decode('utf-8', 'ignore')
        eval('mqtt_topic_' + bytes.decode(ubinascii.hexlify(topic)) + '("' + _msg + '")')
    except: print((topic, msg))

mqtt.set_callback(mqtt_callback)

mqtt.subscribe("mpython/001")

def timer14_tick(_):
    mqtt.ping()

tim14 = Timer(14)
tim14.init(period=20000, mode=Timer.PERIODIC, callback=timer14_tick)


mqtt.publish("mpython/001", "hello")
while True:
    mqtt.wait_msg()
