from mpython import*
import json

import urequests                    #用于网络访问的模块
from seniverse import *             #天气图标模块
from machine import Timer           #定时器模块
from umqtt.simple import MQTTClient
from machine import Timer
import ubinascii


API_KEY = 'jd41hnij4ffx2hwl'                 #心知天气API密钥（key）

url_now="https://api.seniverse.com/v3/weather/now.json"           #获取天气实况的请求地址
url_daily="https://api.seniverse.com/v3/weather/daily.json"       #获取多日天气预报的请求地址

oled.DispChar('联网中...',40,25)     #OLED屏显示联网提示
oled.show()

mywifi=wifi()
mywifi.connectWiFi('abcd','1234567890')          #连接 WiFi 网络

'''
lot部分
'''

def nowWeather(apikey,location='金华',language='zh-Hans',unit='c'):         #设置天气实况返回的数据
    nowResult = urequests.get(url_now, params={
        'key': apikey,
        'location': location,
        'language': language,
        'unit': unit
    })
    json=nowResult.json()
    nowResult.close()
    return json

def dailyWeather(apikey,location='金华',language='zh-Hans',unit='c',start='0',days='5'):        #设置多日天气，只返回今日的数据
    dailyResult = urequests.get(url_daily, params={
        'key': apikey,
        'location': location,
        'language': language,
        'start': start,
        'days': days
    })
    json=dailyResult.json()
    dailyResult.close()
    return  json


def refresh(cs):
    nowRsp=nowWeather(API_KEY,cs)                 #通过API密钥获取天气实况
    dailyRsp=dailyWeather(API_KEY,cs)             #通过API密钥获取多日天气预报
    print(nowRsp)

    today=dailyRsp['results'][0]['daily'][0]['date'][-5:]         #当前日期，显示“月-日”
    todayHigh=dailyRsp['results'][0]['daily'][0]['high']          #最高温度
    todaylow=dailyRsp['results'][0]['daily'][0]['low']            #最低温度

    nowText=nowRsp['results'][0]['now']['text']                   #天气现象文字
    nowTemper=nowRsp['results'][0]['now']['temperature']          #温度
    todayIco=nowRsp['results'][0]['now']['code']                  #天气现象图标
    city=nowRsp['results'][0]['location']['name']                 #地理位置

    oled.fill(0)
    oled.Bitmap(10,23,ico[todayIco],38,38,1)                   #显示当前天气现象图标
    oled.DispChar("%s,天气实况" %city,0,0)
    oled.DispChar(today,90,0)
    oled.DispChar("%s℃/%s" %(nowTemper,nowText),70,25)        #显示当前温度
    oled.DispChar("%s~%s℃" %(todaylow,todayHigh),70,45)       #显示今日最低、最高气温
    oled.show()

'''
'''
mqtt = MQTTClient("0805e3d04f3b34e7", "192.168.18.4", 1883, "siot", "dfrobot", keepalive=30) #创建MQTT对象
try:
    mqtt.connect()
    print('Connected')
except:
    print('Disconnected')
def mqtt_topic_706a7a782f78786a73(_msg):   #接收信息并处理
    cs = str(_msg)
    refresh(cs)                            #调用显示气象信息函数
def mqtt_callback(topic, msg):
    try:
        topic = topic.decode('utf-8', 'ignore')
        _msg = msg.decode('utf-8', 'ignore')
        eval('mqtt_topic_' + bytes.decode(ubinascii.hexlify(topic)) + '("' + _msg + '")')
    except: print((topic, msg))
mqtt.set_callback(mqtt_callback)
mqtt.subscribe("pjzx/xxjs")               #项目名称/设备名称
def timer14_tick(_):
    mqtt.ping()
tim14 = Timer(14)
tim14.init(period=20000, mode=Timer.PERIODIC, callback=timer14_tick)
while True:
    mqtt.wait_msg()
