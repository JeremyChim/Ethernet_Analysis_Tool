
from math import ceil

def csv():

    # 配置参数
    a = ' ,INS_Vehicle_Heading,INS_Vehicle_Heading_Accuracy,INS_Vehicle_Heading_Confidence,INS_Vehicle_Height_Confidence,INS_Vehicle_Lat_Confidence,INS_Vehicle_Lat,INS_Vehicle_Lat_Err,INS_Vehicle_Lon_Confidence,INS_Vehicle_Lon,INS_Vehicle_Lon_Err,INS_Vehicle_Pitch,INS_Vehicle_Pitch_Accuracy,INS_Vehicle_Pitch_Confidence,INS_Vehicle_Roll,INS_Vehicle_Roll_Accuracy,INS_Vehicle_Roll_Confidence,INS_Vehicle_Height,INS_Vehicle_Height_Err,INS_Vehicle_Height_Confidence,FL_wheel_vel,FR_wheel_vel,RL_wheel_vel,RR_wheel_vel,RL_wheel_factor,RR_wheel_factor,INS_GPS_Week,INS_GPS_Time,INS_Timestamp,INS_Timestamp_Valid,INS_POS_Match_RTK_POS_Mark,INS_17F_TiDiffer'
    b = [0, 6, 10, 12, 14, 16, 24, 28, 30, 38, 42, 48, 52, 54, 60, 64, 66, 72, 76, 78, 82, 86, 90, 94, 98, 102, 106, 114, 130, 132, 134]
    c = [6, 10, 12, 14, 16, 24, 28, 30, 38, 42, 48, 52, 54, 60, 64, 66, 72, 76, 78, 82, 86, 90, 94, 98, 102, 106, 114, 130, 132, 134, 138]
    d = [0.001, 0.001, 1, 1, 1, 1e-07, 1, 1, 1e-07, 1, 0.001, 0.001, 1, 0.001, 0.001, 1, 0.001, 1, 1, 0.015625, 0.015625, 0.015625, 0.015625, 0.0001, 0.0001, 1, 1, 0.0001, 1, 1, 1]
    e = [0, 0, 0, 0, 0, -90, 0, 0, -180, 0, -180, 0, 0, -90, 0, 0, -1000, 0, 0, -100, -100, -100, -100, 0, 0, 0, 0, 0, 0, 0, 0]

    # 打开log
    f = open('cache/log_17F.txt','r')
    r = f.readlines()
    max = 1000000  # 到多少行分? 1000000
    long = len(r) # log有多少行？
    fen = ceil(long/max) # 分成几份？

    # 创建表头
    ls = [a]
    x = 0

    for i in r:
        da = i[40:] # 去帧头
        ls2 = [x] # 写序号
        x += 1
        for j in range(31):
            da1 = da[b[j]:c[j]] # 切片
            da2 = int(da1, 16) # 16进制转10进制
            da3 = da2 * d[j] + e[j] # 物理值 = 原始值 * 精度 + 偏移量
            ls2.append(da3) # 写入一个数据
        ls.append(ls2) # 写入一整行数据
    f.close()

    # 创建csv
    if fen == 1:
        f2 = open('csv/UDP_MSG_17F.csv', 'w')
        for k in ls:
            k = str(k) # 转文本
            k = k[1:-1] # 去括号
            k.replace(' ','') # 去空格
            k += '\n' # 加换行符
            f2.write(k) # 写入csv
        f2.close()

    # 分csv
    else:
        for i in range(fen):
            n = j = i + 1
            i *= max
            j *= max

            f2 = open(f'csv/UDP_MSG_17F_{n}.csv', 'w')
            for k in ls[i:j]:
                k = str(k)  # 转文本
                k = k[1:-1]  # 去括号
                k.replace(' ', '')  # 去空格
                k += '\n'  # 加换行符
                f2.write(k) # 写入csv
            f2.close()

if __name__ == '__main__':

    csv()