# -*- coding: utf-8 -*-
# @Time ： 2023/5/15 16:42
# @Auth ： JeremyChim
# @File ：data_flier.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim

def log_1():

    file = open('log.txt', 'r', encoding='gbk', errors='ignore')
    file1 = open('log_0011.txt','w')

    for text in file.readlines():
        key = text[:4]
        if key == '0011':
            file1.write(text)

    file.close()
    file1.close()

def log_146():
    file = open('log_0011.txt', 'r', encoding='gbk', errors='ignore')
    file1 = open('log_146.txt', 'w')

    for text in file.readlines():
        key = text[16:24]
        if key == '00000146':
            file1.write(text)

    file.close()
    file1.close()

log_146()