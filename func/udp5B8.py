# -*- coding: utf-8 -*-
# @Time ： 2023/6/19 14:21
# @Auth ： JeremyChim
# @File ：udp5B8.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from math import ceil

def csv():
    # 配置参数
    a = ' ,INSHwVers0,INSHwVers1,INSHwVers2,INSHwVers3,INSHwVers4,INSHwVers5,INSHwVers6,INSSwVers0,INSSwVers1,INSSwVers2,INSSwVers3,INSSwVers4,INSSwVers5,INSSwVers6,Packet_Count '
    b = [0, 2, 4, 6, 8, 12, 14, 16, 18, 20, 22, 24, 28, 30]
    c = [2, 4, 6, 8, 12, 14, 16, 18, 20, 22, 24, 28, 30, 32]
    d = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    f = open('cache/log_5B8.txt', 'r')
    r = f.readlines()

    max = 1000000  # 到多少行分? 1000000
    long = len(r)  # log有多少行？
    fen = ceil(long / max)  # 分成几份？

    x = 0

    for i in range(fen):
        ls = [a]  # 创建表头
        n = j = i + 1
        i *= max # 前索引
        j *= max # 后索引

        if fen == 1:
            f2 = open('csv/UDP_MSG_5B8.csv', 'w')
        else:
            f2 = open(f'csv/UDP_MSG_5B8_{n}.csv', 'w')

        for i in r[i:j]:
            da = i[40:]  # 去帧头
            da4 = int(i[4:8], 16)  # 流水号
            ls2 = [x]  # 写序号
            x += 1

            for j in range(14):
                da1 = da[b[j]:c[j]]  # 切片
                da2 = int(da1, 16)  # 16进制转10进制
                da3 = da2 * d[j] + e[j]  # 物理值 = 原始值 * 精度 + 偏移量
                ls2.append(da3)  # 写入一个数据
            ls2.append(da4)  # 写入流水号
            ls.append(ls2)  # 写入一整行数据

        for k in ls:
            k = str(k)  # 转文本
            k = k[1:-1]  # 去括号
            k.replace(' ', '')  # 去空格
            k += '\n'  # 加换行符
            f2.write(k)  # 写入csv

        f2.close()
    f.close()

if __name__ == '__main__':
    from time import time
    a = time()
    csv()
    b = time()
    c = '%.2f' % float(b-a)
    print(f'运行时间：{c}秒')