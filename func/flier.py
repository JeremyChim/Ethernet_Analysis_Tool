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

def log_5B3():
    '''将0x17F的数据，保存成txt'''
    f = open('cache/log_0011.txt', 'r', encoding='gbk', errors='ignore')
    f1 = open('cache/log_5B3.txt', 'w')
    f2 = open('cache/error_log.txt','a')
    r = f.readlines()

    for i in r:
        j = i[16:24]
        l = len(i)
        if j == '000005b3':
            if l == 59:
                f1.write(i)
            else:
                f2.write(i)

    f.close()
    f1.close()
    f2.close()

def log_rel():
    '''将0x17F和0x146的数据，保存成txt，用来处理成rel表'''

    f1 = open('cache/log_17F.txt','r')
    f2 = open('cache/log_146.txt', 'r')
    f3 = open('cache/log_rel.txt', 'w')

    r1 = f1.readlines()
    r2 = f2.readlines()
    ls1 = []
    ls2 = []

    for i in r1:
        da = i[40:]
        da2 = da[106:114] # 17F:INS_GPS_Time
        ls1.append(da2)

    for i in r2:
        da = i[40:]
        da2 = da[194:] # 146:最后7个元素
        ls2.append(da2)

    j = 0
    for i in ls1:
        k = i + ls2[j]
        f3.write(k)
        j += 1

    f1.close()
    f2.close()
    f3.close()

if __name__ == '__main__':
    # path = 'log.txt'
    # log_0011(path)
    # log_146()
    # log_17F()
    # log_31B()
    log_5B3()
    # log_rel()