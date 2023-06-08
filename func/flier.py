# -*- coding: utf-8 -*-
# @Time ： 2023/5/15 16:42
# @Auth ： JeremyChim
# @File ：flier.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim

def log_0011(path):
    '''将0011开头的数据，保存成txt
    :param path:原始数据log的路径
    '''

    f = open(path, 'r', encoding='gbk', errors='ignore')
    f1 = open('cache/log_0011.txt','w')
    r = f.readlines()

    for i in r:
        j = i[:4]
        if j == '0011':
            f1.write(i)

    f.close()
    f1.close()

def log_146():
    '''将0x146的数据，保存成txt'''
    f = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    f1 = open('cache/log_146.txt', 'w')
    f2 = open('cache/error_log.txt', 'a')
    r = f.readlines()

    for i in r:
        j = i[16:24]
        l = len(i)
        if j == '00000146':
            if l == 279:
                f1.write(i)
            else:
                f2.write(i)

    f.close()
    f1.close()
    f2.close()

def log_17F():
    '''将0x17F的数据，保存成txt'''
    f = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    f1 = open('cache/log_17F.txt', 'w')
    f2 = open('cache/error_log.txt','a')
    r = f.readlines()

    for i in r:
        j = i[16:24]
        l = len(i)
        if j == '0000017f':
            if l == 179:
                f1.write(i)
            else:
                f2.write(i)

    f.close()
    f1.close()
    f2.close()

def log_31B():
    '''将0x31B的数据，保存成txt'''
    f = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    f1 = open('cache/log_31B.txt', 'w')
    f2 = open('cache/error_log.txt', 'a')
    r = f.readlines()

    for i in r:
        j = i[16:24]
        l = len(i)
        if j == '0000031b':
            if l == 153:
                f1.write(i)
            else:
                f2.write(i)

    f.close()
    f1.close()
    f2.close()

if __name__ == '__main__':
    path = 'log.txt'
    log_0011(path)
    log_146()
    log_17F()
    log_31B()