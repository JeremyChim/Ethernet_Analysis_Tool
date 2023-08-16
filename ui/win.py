# -*- coding: utf-8 -*-
# @Time ： 2023/5/24 15:50
# @Auth ： JeremyChim
# @File ：win.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

# 外部函数调用（指定函数）
from ttkbootstrap.constants import *
from windnd import hook_dropfiles
from tkinter import filedialog
from tkinter.messagebox import showinfo
from time import sleep
from os import path as pa
from os import mkdir
from threading import Thread
from random import randint

import ttkbootstrap as ttk

# 自定义函数调用
import func.flier as fl
import func.udp17F_v20 as u17F_v20
import func.udp17F_v19 as u17F_v19
import func.udp17F_v18 as u17F_v18
import func.udp31B as u31B
import func.udp146 as u146
import func.udp5B3 as u5B3
import func.udp5B8 as u5B8
import func.udp271 as u271
import func.rel as rel

# 类
class app(ttk.Frame):
    def __init__(self, win):
        super().__init__(win) # app = ttk.Frame(win)
        self.pack() # app.pack()

        # 容器
        self.sv_theme = ttk.StringVar()     # 主题名
        self.sv_log_path = ttk.StringVar()  # log路径
        self.iv_ver = ttk.IntVar(value=20)  # 协议
        self.iv_17f = ttk.IntVar(value=1)   # 17F
        self.iv_146 = ttk.IntVar(value=1)   # 146
        self.iv_31b = ttk.IntVar(value=0)   # 31B
        self.iv_rel = ttk.IntVar(value=0)   # rel
        self.iv_5b3 = ttk.IntVar(value=0)   # 5B3
        self.iv_5b8 = ttk.IntVar(value=0)  # 5B8
        self.iv_271 = ttk.IntVar(value=0)  # 271
        self.iv_pg = ttk.IntVar(value=0)    # 进度条

        # 外框
        f = ttk.Frame(padding=10)
        f.pack(fill=X, expand=YES, anchor=N)

        # 拖入读取
        hook_dropfiles(f, func=self.fun_load)

        # 内框
        self.f2 = ttk.Frame(f, padding=10)
        self.lf = ttk.LabelFrame(f, text='日志', padding=10)
        self.lf4 = ttk.LabelFrame(f, text='协议', padding=10)
        self.lf2 = ttk.LabelFrame(f, text='信号', padding=10)
        self.lf3 = ttk.LabelFrame(f, text='操作', padding=10)

        self.f2.pack(fill=X, expand=YES)
        self.lf.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf4.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf2.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf3.pack(fill=X, expand=YES)

        # 行
        self.row_theme()
        self.row_load()
        self.row_ver()
        self.row_sgn()
        self.row_exec()

    def row_theme(self):
        '''主题栏'''
        f = self.f2
        sv = self.sv_theme
        s = ttk.Style()
        tn = s.theme_names()
        i = tn.index(s.theme.name) # 初始索引值：morph主题为 9
        # print(i)

        b = ttk.Button(f, text='关于', command=self.fun_about)
        l = ttk.Label(f, text='主题')
        self.tm = ttk.Combobox(f, width=15, values=tn, textvariable=sv)
        self.tm.current(i) # 初始主题
        b2 = ttk.Button(f, text='应用', command=self.fun_theme)
        b3 = ttk.Button(f, text='☀', command=self.fun_theme_day)
        b4 = ttk.Button(f, text='☾', command=self.fun_theme_night)

        b.pack(side=LEFT, padx=(0, 0))
        b3.pack(side=LEFT, padx=(10, 0))
        b4.pack(side=LEFT, padx=(10, 0))
        b2.pack(side=RIGHT, padx=(10, 0))
        self.tm.pack(side=RIGHT, padx=(10, 0))
        l.pack(side=RIGHT, padx=(10, 0))

    def row_load(self):
        '''加载栏'''
        lf = self.lf
        sv = self.sv_log_path

        l = ttk.Label(lf, text='路径')
        e = ttk.Entry(lf, width=40, textvariable=sv)
        b = ttk.Button(lf, text='浏览', width=10, command=self.fun_open)

        l.pack(side=LEFT, padx=10)
        e.pack(side=LEFT, padx=10, fill=X, expand=YES)
        b.pack(side=LEFT, padx=10)

    def row_ver(self):
        '''协议栏'''
        lf = self.lf4
        iv = self.iv_ver

        rb = ttk.Radiobutton(lf, text='v1.8', variable=iv, value=18)
        rb2 = ttk.Radiobutton(lf, text='v1.9', variable=iv, value=19)
        rb3 = ttk.Radiobutton(lf, text='v2.0', variable=iv, value=20)

        rb.pack(side=LEFT, padx=10)
        rb2.pack(side=LEFT, padx=10)
        rb3.pack(side=LEFT, padx=10)

    def row_sgn(self):
        '''信号栏'''
        lf = self.lf2
        iv = self.iv_17f
        iv2 = self.iv_31b
        iv3 = self.iv_146
        iv4 = self.iv_rel
        iv5 = self.iv_5b3
        iv6 = self.iv_5b8
        iv7 = self.iv_271

        cb = ttk.Checkbutton(lf,text='17F', variable=iv, onvalue=1, offvalue=0)
        cb2 = ttk.Checkbutton(lf,text='31B', variable=iv2, onvalue=1, offvalue=0)
        cb3 = ttk.Checkbutton(lf,text='146', variable=iv3, onvalue=1, offvalue=0)
        cb4 = ttk.Checkbutton(lf, text='REL', variable=iv4, onvalue=1, offvalue=0)
        cb5 = ttk.Checkbutton(lf, text='5B3', variable=iv5, onvalue=1, offvalue=0)
        cb6 = ttk.Checkbutton(lf, text='5B8', variable=iv6, onvalue=1, offvalue=0)
        cb7 = ttk.Checkbutton(lf, text='271', variable=iv7, onvalue=1, offvalue=0)

        cb.pack(side=LEFT, padx=10)
        cb3.pack(side=LEFT, padx=10)
        cb2.pack(side=LEFT, padx=10)
        cb5.pack(side=LEFT, padx=10)
        cb6.pack(side=LEFT, padx=10)
        cb7.pack(side=LEFT, padx=10)
        cb4.pack(side=LEFT, padx=10)

    def row_exec(self):
        '''执行栏'''
        lf = self.lf3
        iv = self.iv_pg

        self.b = ttk.Button(lf, text='生成csv', command=self.fun_thread)
        self.pb = ttk.Progressbar(lf, maximum=100, variable=iv, bootstyle='success-striped')

        self.b.pack(padx=10, fill=X, expand=YES)
        self.pb.pack(padx=10, fill=X, expand=YES)

    def fun_about(self):
        '''关于'''
        showinfo('关于 以太网报文解析工具',
                               '作者：Jer小铭😎 \n'
                               '技术支持：Mavis🤣 \n'
                               '建议提供：少基同学🤪 \n'
                               '思路提供：家文同学😏 \n'
                               '测试验证：少丽同学🤨 \n'
                               '缺陷提出：莲花同学🤓 \n'
                               '开发指导：媛媛同学🤠 \n'
                               '技术指导：坚莲大佬🧐 \n\n' 
                               '感谢各位同学和大佬的支持。^0^'
                               )


    def fun_theme_day(self):
        '''白天模式'''
        s = ttk.Style()
        a = randint(1, 10)

        match a % 5:
            case 0:
                cb = 'minty'
            case 1:
                cb = 'united'
            case 2:
                cb = 'morph'
            case 3:
                cb = 'cosmo'
            case 4:
                cb = 'pulse'

        s.theme_use(cb)
        print(f'应用主题:{cb}')


    def fun_theme_night(self):
        '''夜间模式'''
        s = ttk.Style()
        a = randint(1, 10)

        match a % 5:
            case 0:
                cb = 'darkly'
            case 1:
                cb = 'superhero'
            case 2:
                cb = 'solar'
            case 3:
                cb = 'cyborg'
            case 4:
                cb = 'vapor'

        s.theme_use(cb)
        print(f'应用主题:{cb}')

    def fun_theme(self):
        '''应用主题'''
        s = ttk.Style()
        cb = self.tm.get()

        s.theme_use(cb)
        print(f'应用主题:{cb}')

    def fun_open(self):
        '''浏览文件'''
        sv = self.sv_log_path
        path = filedialog.askopenfilename(title='选择日志文件')
        if path:
            sv.set(path)

    def fun_exec(self):
        '''生成csv'''
        theme = self.sv_theme.get()
        log_path = self.sv_log_path.get()
        ver = self.iv_ver.get()
        io_17f = self.iv_17f.get()
        io_146 = self.iv_146.get()
        io_31b = self.iv_31b.get()
        io_5b3 = self.iv_5b3.get()
        io_5b8 = self.iv_5b8.get()
        io_271 = self.iv_271.get()
        io_rel = self.iv_rel.get()

        sum = io_17f + io_146 + io_31b + io_5b3 + io_5b8 + io_271 + io_rel
        mul = sum * 2
        pg_val = int(60 / mul)

        update = self.fun_pg_thread  # 进度条更新函数
        b = self.b  # 按钮

        print(f'当前设定:\n'
              f'主题:{theme}\n'
              f'路径:{log_path}\n'
              f'协议:{ver}\n'
              f'17F:{io_17f}\n'
              f'146:{io_146}\n'
              f'31B:{io_31b}\n'
              f'5B3:{io_5b3}\n'
              f'rel:{io_rel}\n')

        # 创建cache文件夹
        if not pa.exists('cache'):
            mkdir('cache')

        # 过滤数据
        fl.log_0011(log_path), update(30, '筛选0011数据中...')

        # 创建csv文件夹
        if not pa.exists('csv'):
            mkdir('csv')

        # 输出

        if io_17f == 1:
            match ver:
                case 18:
                    fl.log_17F_v18(), update(pg_val, '17F数据处理中...')
                    u17F_v18.csv(), update(pg_val, '17F数据生成中...')
                case 19:
                    fl.log_17F_v19(), update(pg_val, '17F数据处理中...')
                    u17F_v19.csv(), update(pg_val, '17F数据生成中...')
                case 20:
                    fl.log_17F_v20(), update(pg_val, '17F数据处理中...')
                    u17F_v20.csv(), update(pg_val, '17F数据生成中...')

        if io_146 == 1:
            fl.log_146(), update(pg_val, '146数据处理中...')
            u146.csv(), update(pg_val, '146生成处理中...')

        if io_31b == 1:
            fl.log_31B(), update(pg_val, '31B数据处理中...')
            u31B.csv(), update(pg_val, '31B数据生成中...')

        if io_5b3 == 1:
            fl.log_5B3(), update(pg_val, '5B3数据处理中...')
            u5B3.csv(), update(pg_val, '5B3生成处理中...')

        if io_5b8 == 1:
            fl.log_5B8(), update(pg_val, '5B8数据处理中...')
            u5B8.csv(), update(pg_val, '5B8生成处理中...')

        if io_271 == 1:
            fl.log_271(), update(pg_val, '271数据处理中...')
            u271.csv(), update(pg_val, '271生成处理中...')

        if io_rel == 1:
            if not pa.exists('cache/log_17F.txt'):
                match ver:
                    case 18:
                        fl.log_17F_v18(), update(pg_val, '17F数据处理中...')
                        u17F_v18.csv(), update(pg_val, '17F数据生成中...')
                    case 19:
                        fl.log_17F_v19(), update(pg_val, '17F数据处理中...')
                        u17F_v19.csv(), update(pg_val, '17F数据生成中...')
                    case 20:
                        fl.log_17F_v20(), update(pg_val, '17F数据处理中...')
                        u17F_v20.csv(), update(pg_val, '17F数据生成中...')

            if not pa.exists('cache/log_146.txt'):
                fl.log_146(), update(pg_val, '146数据处理中...')
                u146.csv(), update(pg_val, '146生成处理中...')

            fl.log_rel(), update(pg_val, 'rel数据处理中...')
            rel.csv(), update(pg_val, 'rel数据处理中...')

        update(10, 'csv文件生成中...')

        self.iv_pg.set(100) # 进度条跑满
        b['text'] = 'csv文件已生成^0^'

        # 弹窗提示
        showinfo('(*^▽^*) Yeah~','csv文件已生成在根目录')
        b.config(state=NORMAL)

        # 初始化进度条
        self.iv_pg.set(0)   # 进度条归零
        b['text'] = '生成csv'


    def fun_thread(self):
        '''建立线程，防假死'''
        fun = self.fun_exec
        t1 = Thread(target=fun)
        print('主线程启动...')
        t1.start()


    def fun_pg_thread(self, pg_val, text):
        '''进度条更新进程'''
        fun = self.fun_pg_update
        th = Thread(target=fun, args=[pg_val, text])
        print(f'子线程启动...{text}')
        th.start()
        th.join()


    def fun_pg_update(self, pg_val, text):
        '''新的进度条'''
        val = self.iv_pg.get()

        for i in range(pg_val):
            val += 1
            if val > 100:
                break

            self.iv_pg.set(val)
            self.pb.update()
            self.b['text'] = f'进度:{val}% {text}'  # 修改按钮文本
            sleep(0.01)

    # def fun_pg_update(self, i, j, l):
    #     '''进度条更新'''
    #     pb = self.pb # 进度条
    #     b = self.b # 按钮
    #     j = j + 2
    #     for k in range(i, j):
    #         pb['value'] = k  # 修改进度
    #         pb.update()
    #         b['text'] = f'进度:{k}% {l}' # 修改按钮文本
    #         sleep(0.01)

    def fun_load(self, path):
        '''拖入读取'''
        sv = self.sv_log_path
        p = '\n'.join((item.decode('gbk') for item in path))
        sv.set(p)

if __name__ == '__main__':
    win = ttk.Window('----------调试窗口----------','litera')
    win.geometry('+640+340')
    app(win)
    lab = ttk.Label(text='----------版本：Demo----------')
    lab.pack(side=RIGHT, padx=10)
    win.mainloop()
