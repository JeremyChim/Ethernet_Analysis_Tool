import datetime

def save_log():
    t = str(datetime.datetime.now())
    t = t.replace('-','')\
        .replace(':','')
    logname = 'log_'+ t[:8] + '_' + t[9:15]
    # print(logname)

    f = open(logname,'w')
    for i in range(100):
        print(str(i), file=f)
    f.close()

if __name__ == '__main__':
    save_log()