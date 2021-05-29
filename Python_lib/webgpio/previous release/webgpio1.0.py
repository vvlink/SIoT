#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: james,yyp,xiezuoru
@version: 1.0
"""
import threading #导入threading模块
from flask import Flask
from flask import request
from xugu import Pin
from xugu import Servo
import time
import json

app = Flask(__name__)
ret = None
pin = None
types = None
pin_D_list=['D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13']
pin_A_list=['A0','A1','A2','A3','A4','A5']
type_D_list=['digital','1']
type_A_list=['analog','2']
type_S_list=['servo','3']

@app.route('/',methods=["POST","GET"])
def web_gpio():
    if (request.method == 'GET'):
        return web_gpio_get(request)
    elif (request.method=='POST'):
        return web_gpio_post(request)

def web_gpio_get(request):
    global ret,pin
    pin=str.upper(request.values.get("pin"))
    print("pin = ",pin)   
    if not (pin in pin_D_list or pin in pin_A_list):
        data = {"pin":pin,"error_code":1, "msg":"rror,invalid Pin"}
        return json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)
    
    if pin in pin_D_list:
        ret = 0
        time.sleep(0.5)
        data = {"pin":pin,"error_code":0,"msg":str(value)}
        return json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)
    if pin in pin_A_list:
        ret = 1
        time.sleep(0.5)
        data = {"pin":pin,"error_code":0,"msg":str(value)}
        return json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)
        
def web_gpio_post(request):
    global types,pin,value
    pin=str.upper(request.values.get("pin"))
    value=request.values.get("value")
    types=str.lower(request.values.get("type"))                      
    if not (pin in pin_D_list or pin in pin_A_list):
        data = {"pin":pin,"error_code":1,"msg":"error,invalid Pin"}
        return json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)
    try:
        value=int(value)
    except Exception:
        data = {"pin":pin,"error_code":1,"msg":"error,Value is wrong"}
        return json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)
    if not (types in type_D_list or types in type_A_list or types in type_S_list):
        data = {"pin":pin,"error_code":1,"msg":"error,Type is wrong"}
        return json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)
    data = {"pin":pin,"error_code":0,"msg":"success,set "+pin+" to "+str(value)+" with "+types+" mode"} 
    return json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)

def xugu():
    global value,ret,types
    while True:
        if ret == 0:    
            xugu_pin=Pin(pin,Pin.IN)
            value=xugu_pin.read_digital()
            ret = None
        if ret == 1:
            xugu_pin=Pin(pin,Pin.ANALOG)
            value=xugu_pin.read_analog()
            ret = None
        if types in type_D_list:
            xugu_pin=Pin(pin,Pin.OUT)
            if value == 0:
                xugu_pin.write_digital(value)
            else:
                value = 1
                xugu_pin.write_digital(value)
            types=None
        if types in type_A_list:
            xugu_pin=Pin(pin,Pin.OUT)
            xugu_pin.write_analog(value)
            types=None
        if types in type_S_list:
            xugu_servo=Servo(pin)
            xugu_servo.write_angle(value)
            types=None
             
def run():
    app.run(host='0.0.0.0',port=1024,debug=False)   

t=threading.Thread(target=run)
t.start()

xugu()

