
from math import ceil

def csv():

    # 配置参数
    a = ' ,INS_Vehicle_X_Acc,INS_Vehicle_X_Rate,INS_Vehicle_Y_Acc,INS_Vehicle_Y_Rate,INS_Vehicle_Z_Acc,INS_Vehicle_Z_Rate,INS_IMU_Time,INS_IMU_Valid,INS_IMU_X_Acc_Bias,INS_IMU_X_Rate_Bias,INS_IMU_Y_Acc_Bias,INS_IMU_Y_Rate_Bias,INS_IMU_Z_Acc_Bias,INS_IMU_Z_Rate_Bias,INS_Vehicle_Quaternion_W,INS_Vehicle_Quaternion_X,INS_Vehicle_Quaternion_Y,INS_Vehicle_Quaternion_Z,IMU_to_Vehicle_Offset_X,IMU_to_Vehicle_Offset_Y,IMU_to_Vehicle_Offset_Z,INS_Timestamp,INS_Timestamp_Valid,INS_146_TiDiffer,INS_IMU_X_Acc,INS_IMU_X_Rate,INS_IMU_Y_Acc,INS_IMU_Y_Rate,INS_IMU_Z_Acc,INS_IMU_Z_Rate,IMU_to_Vehicle_Error_Quaternion_W,IMU_to_Vehicle_Error_Quaternion_X,IMU_to_Vehicle_Error_Quaternion_Y,IMU_to_Vehicle_Error_Quaternion_Z,SlowDr_Status,INS_Vehicle_SlowDr_Pos_X,INS_Vehicle_SlowDr_Pos_Y,INS_Vehicle_SlowDr_Pos_Z,INS_Vehicle_SlowDr_Roll,INS_Vehicle_SlowDr_Pitch,INS_Vehicle_SlowDr_Heading'
    b = [0, 6, 12, 18, 24, 30, 36, 44, 46, 50, 54, 58, 62, 66, 70, 76, 82, 88, 94, 100, 106, 112, 128, 130, 134, 140, 146, 152, 158, 164, 170, 176, 182, 188, 194, 196, 204, 212, 220, 226, 232]
    c = [6, 12, 18, 24, 30, 36, 44, 46, 50, 54, 58, 62, 66, 70, 76, 82, 88, 94, 100, 106, 112, 128, 130, 134, 140, 146, 152, 158, 164, 170, 176, 182, 188, 194, 196, 204, 212, 220, 226, 232, 238]
    d = [0.001, 1.7452e-05, 0.001, 1.7452e-05, 0.001, 1.7452e-05, 1, 1, 0.001, 1.7452e-05, 0.001, 1.7452e-05, 0.001, 1.7452e-05, 1e-06, 1e-06, 1e-06, 1e-06, 0.0001, 0.0001, 0.0001, 0.0001, 1, 1, 0.001, 1.7452e-05, 0.001, 1.7452e-05, 0.001, 1.7452e-05, 1e-06, 1e-06, 1e-06, 1e-06, 1, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
    e = [-40, -4.363, -40, -4.363, -40, -4.363, 0, 0, -10, -0.17452, -10, -0.17452, -10, -0.17452, -1, -1, -1, -1, -5, -5, -5, 0, 0, 0, -40, -4.363, -40, -4.363, -40, -4.363, -1, -1, -1, -1, 0, -2147483.647, -2147483.647, -2147483.647, -90, -180, 0]

    # 打开log
    f = open('cache/log_146.txt','r')
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
        for j in range(41):
            da1 = da[b[j]:c[j]] # 切片
            da2 = int(da1, 16) # 16进制转10进制
            da3 = da2 * d[j] + e[j] # 物理值 = 原始值 * 精度 + 偏移量
            ls2.append(da3) # 写入一个数据
        ls.append(ls2) # 写入一整行数据
    f.close()

    # 创建csv
    if fen == 1:
        f2 = open('csv/UDP_MSG_146.csv','w')
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

            f2 = open(f'csv/UDP_MSG_146_{n}.csv', 'w')
            for k in ls[i:j]:
                k = str(k)  # 转文本
                k = k[1:-1]  # 去括号
                k.replace(' ', '')  # 去空格
                k += '\n'  # 加换行符
                f2.write(k)  # 写入csv
            f2.close()

if __name__ == '__main__':

    csv()