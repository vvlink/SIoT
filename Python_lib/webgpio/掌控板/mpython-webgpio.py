from mpython import *
import time
import urequests
import json
import network

def on_button_a_down(_):
    global v
    time.sleep_ms(10)
    if button_a.value() == 1: return
    _response = urequests.post('http://192.168.3.42:1024', headers={"Content-Type":"application/json"}, data=json.dumps({"pin":'D13', "value":str(v), "type":'1'}))
    v = 1 - v
    oled.fill_rect(0, 16, 128, 16, 0)
    oled.DispChar(_response.json().get('msg'), 0, 16, 1)
    oled.show()

def on_button_b_down(_):
    time.sleep_ms(10)
    if button_b.value() == 1: return
    _response = urequests.get('http://192.168.3.42:1024', headers={"Content-Type":"application/json"}, data=json.dumps({"pin":'A0'}))
    oled.fill_rect(0, 48, 128, 16, 0)
    oled.DispChar(('A0的值为：' + str(_response.json().get('msg'))), 0, 48, 1)
    oled.show()

v = 1
my_wifi = wifi()
my_wifi.connectWiFi('jf', '12345678')
button_a.irq(trigger=Pin.IRQ_FALLING, handler=on_button_a_down)
button_b.irq(trigger=Pin.IRQ_FALLING, handler=on_button_b_down)
oled.DispChar('按A键控制虚谷号13口', 0, 0, 1)
oled.show()

