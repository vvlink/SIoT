#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: xiezuoru
### 调用GET方法，读取A0号引脚的电平。
在该案例中可以修改的参数有:
    - url:设置成虚谷号的IP地址
    - pin:对应的引脚 A0-A5，D0-D13
注意：该方法需要外接传感器，否则数字口默认返回为低电平，模拟口返回随机数。
"""
import requests

vvboardip='192.168.3.14'
pin='A1'
payload = {"pin":pin}
re = requests.get(url='http://'+ vvboardip +':1024/',params=payload)
if (re.status_code==200):
    r=re.json()
    print('返回的原始信息为：')
    print(re.text)
    print('成功获取引脚'+ str(r.get("pin")) + '的状态:'+ str(r.get("msg")))
