# -*- coding: utf-8 -*-
# @Time ： 2023/6/10 0:51
# @Auth ： JeremyChim
# @File ：rel.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/
def csv():

    # 配置参数
    a = 'INS_GPS_Time,SlowDr_Status,INS_Vehicle_SlowDr_Pos_X,INS_Vehicle_SlowDr_Pos_Y,INS_Vehicle_SlowDr_Pos_Z,INS_Vehicle_SlowDr_Pitch,INS_Vehicle_SlowDr_Roll,INS_Vehicle_SlowDr_Heading'
    b = [0, 8, 10, 18, 26, 40, 34, 46]
    c = [8, 10, 18, 26, 34, 46, 40, 52]
    d = [1, 1, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
    e = [0, 0, -2147483.647, -2147483.647, -2147483.647, -180, -90, 0]

    # 最后第二和最后第三所有元素都互换一下（INS_Vehicle_SlowDr_Pitch 和 INS_Vehicle_SlowDr_Roll互换）

    # 打开log
    f = open('cache/log_rel.txt','r')
    r = f.readlines()

    # 创建表头
    ls = [a]

    for i in r:
        ls2 = []
        for j in range(8):
            da1 = i[b[j]:c[j]] # 切片
            da2 = int(da1, 16) # 16进制转10进制
            da3 = da2 * d[j] + e[j] # 物理值 = 原始值 * 精度 + 偏移量
            ls2.append(da3) # 写入一个数据
        ls.append(ls2) # 写入一整行数据
    f.close()

    # 创建csv
    f2 = open('csv/rel.csv','w')

    for k in ls:
        k = str(k) # 转文本
        k = k[1:-1] # 去括号
        k.replace(' ','') # 去空格
        k = k + '\n' # 加换行符
        f2.write(k) # 写入csv
    f2.close()

if __name__ == '__main__':

    csv()