# -*- coding: utf-8 -*-
# @Time ： 2023/5/16 15:21
# @Auth ： JeremyChim
# @File ：app.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim

import os
import func.flier as fl
import func.udp17F as u17F
import func.udp31B as u31B
import func.udp146 as u146

# 创建cache文件夹
if not os.path.exists('cache'):
    os.mkdir('cache')

# 过滤数据
path = 'log.txt'
fl.log_0011(path), print('1/7 log_0011完成')
fl.log_146(), print('2/7 log_146完成')
fl.log_17F(), print('3/7 log_17F完成')
fl.log_31B(), print('4/7 log_31B完成')

# 创建csv文件夹
if not os.path.exists('csv'):
    os.mkdir('csv')

# 输出csv
u146.csv(), print('5/7 csv_146完成')
u17F.csv(), print('6/7 csv_17F完成')
u31B.csv(), print('7/7 csv_31B完成')

print('Finish. ^-^')


