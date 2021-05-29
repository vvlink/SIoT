from mpython import *
import network
from umqtt.simple import MQTTClient

my_wifi = wifi()
my_wifi.connectWiFi("makerspace", "m@kersp@ce")

mqtt = MQTTClient("zhangkong", "192.168.1.135", 1883, "siot", "dfrobot", keepalive=30)

try:
    mqtt.connect()
    print('Connected')
except:
    print('Disconnected')

def on_button_a_down(_):
    mqtt.publish("mpythonx/001", "A")
    oled.DispChar("A", 0, 48, 1)
    oled.show()

def on_button_b_down(_):
    mqtt.publish("mpythonx/001", "B")
    oled.DispChar("B", 0, 48, 1)
    oled.show()

button_a.irq(trigger=Pin.IRQ_FALLING, handler=on_button_a_down)

button_b.irq(trigger=Pin.IRQ_FALLING, handler=on_button_b_down)


oled.DispChar(my_wifi.sta.ifconfig()[0], 0, 0, 1)
oled.show()
