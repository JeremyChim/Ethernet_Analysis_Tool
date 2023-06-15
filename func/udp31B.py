# -*- coding: utf-8 -*-
# @Time ： 2023/6/15 15:28
# @Auth ： JeremyChim & Mavis
# @File ：udp31B.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from math import ceil

def csv():
    # 配置参数
    a = ' ,INS_GNSS_Time_Year,INS_GNSS_Time_Month,INS_GNSS_Time_Date,INS_GNSS_Time_Hour,INS_GNSS_Time_Minute,INS_GNSS_Time_Second,INS_GNSS_Time_mSecond,GNSS_Speed,GNSS_Speed_Err,INS_GNSS_Speed_North,INS_GNSS_Speed_East,INS_GNSS_Speed_Earth,INS_GNSS_Speed_North_Err,INS_GNSS_Speed_East_Err,INS_GNSS_Speed_Earth_Err,INS_GNSS_Difference_delay,INS_GNSS_GDOP,INS_GNSS_PDOP,INS_GNSS_HDOP,INS_GNSS_VDOP,INS_GNSS_TDOP,INS_GNSS_Speed_East_Confidence,INS_GNSS_Speed_North_Confidence,INS_GNSS_Speed_Earth_Confidence,INS_WatchedSV,INS_UsedSV,INS_GPS_Flight_Path_Angle,INS_GNSS_Time_Valid'
    b = [0, 4, 6, 8, 10, 12, 14, 18, 24, 28, 34, 40, 46, 50, 54, 58, 64, 70, 76, 82, 88, 94, 96, 98, 100, 102, 104, 110]
    c = [4, 6, 8, 10, 12, 14, 18, 24, 28, 34, 40, 46, 50, 54, 58, 64, 70, 76, 82, 88, 94, 96, 98, 100, 102, 104, 110, 112]
    d = [1, 1, 1, 1, 1, 1, 1, 0.001, 1, 0.001, 0.001, 0.001, 1, 1, 1, 0.001, 0.01, 0.01, 0.01, 0.01, 0.01, 1, 1, 1, 1, 1, 0.001, 1]
    e = [2000, 0, 0, 0, 0, 0, 0, -100, 0, -100, -100, -100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -180, 0]

    f = open('cache/log_31B.txt', 'r')
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
            f2 = open('csv/UDP_MSG_31B.csv', 'w')
        else:
            f2 = open(f'csv/UDP_MSG_31B_{n}.csv', 'w')

        for i in r[i:j]:
            da = i[40:]  # 去帧头
            ls2 = [x]  # 写序号
            x += 1

            for j in range(28):
                da1 = da[b[j]:c[j]]  # 切片
                da2 = int(da1, 16)  # 16进制转10进制
                da3 = da2 * d[j] + e[j]  # 物理值 = 原始值 * 精度 + 偏移量
                ls2.append(da3)  # 写入一个数据

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