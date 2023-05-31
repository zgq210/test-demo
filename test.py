# -*- coding: utf-8 -*-
# @Time : 2023-05-30 18:41
# @Author : zgq
# @Email : 1843204521@qq.com
# @File : test.py

from openvino.inference_engine import IECore

ie=IECore()
for device in ie.available_devices:# 查看有哪些设备支持 OpenVino
    print(device)
