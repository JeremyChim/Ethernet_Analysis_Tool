# -*- coding: utf-8 -*-
# @Time ： 2023/5/30 19:10
# @Auth ： JeremyChim
# @File ：id.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

def fun(path):
    f = open(path, 'r', encoding='gbk', errors='ignore')
    f1 = open('id.csv', 'w')
    r = f.readlines()

    for i in r:
        t = i[21:24]
        print(t)
        f1.write(f'{t}\n')

if __name__ == '__main__':
    fun('log_0011.txt')