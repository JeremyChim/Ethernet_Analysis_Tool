
# 配置参数
a = [' ', 'INS_TiStamp', 'INS_TiBas', 'INS_TiLeap', 'INS_TiOut', 'INS_TIleap_Difference']
b = [0, 16, 18, 20, 22]
c = [16, 18, 20, 22, 30]
d = [0.0001, 1, 1, 1, 1]
e = [0, 0, 0, 0, -10000000]

f = open('cache/log_271.txt','r')
r = f.readlines()

# 创建表头
ls = [a]
x = 0

for i in r:
    da = i[40:]
    ls2 = [x]
    x += 1
    for j in range(5):
        da1 = da[b[j]:c[j]]
        da2 = int(da1, 16)
        da3 = da2 * d[j] + e[j]
        ls2.append(da3)
    ls.append(ls2)
f.close()


f2 = open('cache/udp_271.txt','w')
for k in ls:
    k = str(k) # 转文本
    k = k[1:-1] # 去括号
    k.replace(' ','') # 去空格
    k = k + '\n' # 加换行符
    print(k)
    f2.write(k) # 写入
f2.close()
