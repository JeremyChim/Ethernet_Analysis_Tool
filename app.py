# -*- coding: utf-8 -*-
# @Time ： 2023/5/16 16:42
# @Auth ： JeremyChim
# @File ：app.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim

import os
import function.flier as fl

fl.log_0011()
fl.log_146()
fl.log_17F()
fl.log_31B()

import function.udp146
import function.udp17F
import function.udp31B

os.rename('cache/udp_146.txt','UDP_MSG_146.csv')
os.rename('cache/udp_17F.txt','UDP_MSG_17F.csv')
os.rename('cache/udp_31B.txt','UDP_MSG_31B.csv')