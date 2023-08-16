# -*- coding: utf-8 -*-
# @Time ： 2023/6/19 14:21
# @Auth ： JeremyChim
# @File ：udp271.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from math import ceil

def csv():
    # 配置参数
    a = ' ,INS_TiStamp,INS_TiBas,INS_TiLeap,INS_TiOut,INS_TIleap_Difference,Packet_Count '
    b = [0, 16, 18, 20, 22]
    c = [16, 18, 20, 22, 30]
    d = [0.0001, 1, 1, 1, 1]
    e = [0, 0, 0, 0, -10000000]

    f = open('cache/log_271.txt', 'r')
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
            f2 = open('csv/UDP_MSG_271.csv', 'w')
        else:
            f2 = open(f'csv/UDP_MSG_271_{n}.csv', 'w')

        for i in r[i:j]:
            da = i[40:]  # 去帧头
            da4 = int(i[4:8], 16)  # 流水号
            ls2 = [x]  # 写序号
            x += 1

            for j in range(5):
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