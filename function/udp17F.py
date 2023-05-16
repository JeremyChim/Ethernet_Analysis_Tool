
# 配置参数
a = ' ,INS_Vehicle_Heading,INS_Vehicle_Heading_Accuracy,INS_Vehicle_Heading_Confidence,INS_Vehicle_Height_Confidence,INS_Vehicle_Lat_Confidence,INS_Vehicle_Lat,INS_Vehicle_Lat_Err,INS_Vehicle_Lon_Confidence,INS_Vehicle_Lon,INS_Vehicle_Lon_Err,INS_Vehicle_Pitch,INS_Vehicle_Pitch_Accuracy,INS_Vehicle_Pitch_Confidence,INS_Vehicle_Roll,INS_Vehicle_Roll_Accuracy,INS_Vehicle_Roll_Confidence,INS_Vehicle_Height,INS_Vehicle_Height_Err,INS_Vehicle_Height_Confidence,FL_wheel_vel,FR_wheel_vel,RL_wheel_vel,RR_wheel_vel,RL_wheel_factor,RR_wheel_factor,INS_Timestamp,INS_Timestamp_Valid,INS_GPS_Week,INS_GPS_Time,INS_POS_Match_RTK_POS_Mark,INS_17F_TiDiffer'
b = [0, 6, 10, 12, 14, 16, 24, 28, 30, 38, 42, 48, 52, 54, 60, 64, 66, 72, 76, 78, 82, 86, 90, 94, 98, 114, 130, 102, 106, 132, 134]
c = [6, 10, 12, 14, 16, 24, 28, 30, 38, 42, 48, 52, 54, 60, 64, 66, 72, 76, 78, 82, 86, 90, 94, 98, 102, 130, 132, 106, 114, 134, 138]
d = [0.001, 0.001, 1, 1, 1, 1e-07, 1, 1, 1e-07, 1, 0.001, 0.001, 1, 0.001, 0.001, 1, 0.001, 1, 1, 0.015625, 0.015625, 0.015625, 0.015625, 0.0001, 0.0001, 0.0001, 1, 1, 1, 1, 1]
e = [0, 0, 0, 0, 0, -180, 0, 0, -180, 0, -180, 0, 0, -90, 0, 0, -1000, 0, 0, -100, -100, -100, -100, 0, 0, 0, 0, 0, 0, 0, 0]

f = open('cache/log_17F.txt','r')
r = f.readlines()

# 创建表头
ls = [a]
x = 0

for i in r:
    da = i[40:]
    ls2 = [x]
    x += 1
    for j in range(31):
        da1 = da[b[j]:c[j]]
        da2 = int(da1, 16)
        da3 = da2 * d[j] + e[j]
        ls2.append(da3)
    ls.append(ls2)
f.close()


f2 = open('csv/UDP_MSG_17F.csv','w')
for k in ls:
    k = str(k) # 转文本
    k = k[1:-1] # 去括号
    k.replace(' ','') # 去空格
    k = k + '\n' # 加换行符
    print(k)
    f2.write(k) # 写入
f2.close()
