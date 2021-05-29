#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: xiezuoru
调用POST方法，对虚谷号的引脚进行控制，使用params方式。
在该案例中可以修改的参数有:
    - url:设置成虚谷号的IP地址
    - pin:对应的引脚 A0-A5，D0-D13
    - value:对应的数值
    - type:控制的类型可以是1，2，3，分别代表“digital”、“analog”、“servo”
当设置D13号引脚的电平为1，该引脚对应的LED就会亮起。
"""
import requests
import json

vvboardip='192.168.3.14'
pin='D13'
value=1
t=1
payload = {"pin":pin,"value":value,"type":t}
re = requests.post(url='http://'+ vvboardip +':1024/',params=payload)
if (re.status_code==200):
    print('返回的信息为：')
    print(re.text)
    r=re.json()
    print('成功发送控制命令:'+ r.get("msg"))