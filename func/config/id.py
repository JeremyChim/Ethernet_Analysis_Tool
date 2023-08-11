# -*- coding: utf-8 -*-
# @Time ： 2023/5/30 19:10
# @Auth ： JeremyChim
# @File ：id.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

def fun(path):
    f = open(path, 'r', encoding='gbk', errors='ignore')
    # f1 = open('id.csv', 'w')
    r = f.readlines()
    ls = []

    for i in r:
        t = i[21:24]
        ls.append(t)
        # print(t)
        # f1.write(f'{t}\n')
    return ls

def find_duplicates(lst):
    return [x for x in lst if lst.count(x) > 1]

def find_duplicates(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return [k for k, v in d.items() if v > 0]

if __name__ == '__main__':
    ls = fun('log_0011.txt')
    # print(ls)
    # ls = ['17f','271','146','17f']

    dup = find_duplicates(ls)
    print(dup)