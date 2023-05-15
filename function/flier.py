# -*- coding: utf-8 -*-
# @Time ： 2023/5/15 16:42
# @Auth ： JeremyChim
# @File ：flier.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim

def log_0011():
    file = open('log.txt', 'r', encoding='gbk', errors='ignore')
    file1 = open('cache/log_0011.txt','w')

    for text in file.readlines():
        key = text[:4]
        if key == '0011':
            file1.write(text)

    file.close()
    file1.close()

def log_146():
    file = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    file1 = open('cache/log_146.txt', 'w')

    for text in file.readlines():
        key = text[16:24]
        if key == '00000146':
            file1.write(text)

    file.close()
    file1.close()

def log_17F():
    file = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    file1 = open('cache/log_17F.txt', 'w')

    for text in file.readlines():
        key = text[16:24]
        if key == '0000017f':
            file1.write(text)

    file.close()
    file1.close()

def log_31B():
    file = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    file1 = open('cache/log_31B.txt', 'w')

    for text in file.readlines():
        key = text[16:24]
        if key == '0000031b':
            file1.write(text)

    file.close()
    file1.close()

def log_271():
    file = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    file1 = open('cache/log_271.txt', 'w')

    for text in file.readlines():
        key = text[16:24]
        if key == '00000271':
            file1.write(text)

    file.close()
    file1.close()

if __name__ == '__main__':
    log_0011()
    log_146()
    log_17F()
    log_31B()
    log_271()