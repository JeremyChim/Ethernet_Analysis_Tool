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

import ttkbootstrap as ttk

# 自定义函数调用
import func.flier as fl
import func.udp17F as u17F
import func.udp31B as u31B
import func.udp146 as u146
import func.rel as rel

# 类
class app(ttk.Frame):
    def __init__(self, win):
        super().__init__(win) # app = ttk.Frame(win)
        self.pack() # app.pack()

        # 容器
        self.sv = ttk.StringVar() # 主题名
        self.sv2 = ttk.StringVar() # log路径
        self.iv = ttk.IntVar(value=1) # 17F
        self.iv2 = ttk.IntVar(value=1) # 31B
        self.iv3 = ttk.IntVar(value=1) # 146
        self.iv4 = ttk.IntVar(value=0)  # rel

        # 外框
        f = ttk.Frame(padding=10)
        f.pack(fill=X, expand=YES, anchor=N)

        # 拖入读取
        hook_dropfiles(f, func=self.fun6)

        # 内框
        self.f2 = ttk.Frame(f, padding=10)
        self.lf = ttk.LabelFrame(f, text='日志', padding=10)
        self.lf2 = ttk.LabelFrame(f, text='信号', padding=10)
        self.lf3 = ttk.LabelFrame(f, text='操作', padding=10)

        self.f2.pack(fill=X, expand=YES)
        self.lf.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf2.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf3.pack(fill=X, expand=YES)

        # 行
        self.row()
        self.row2()
        self.row3()
        self.row4()

    def row(self):
        '''主题栏'''
        f = self.f2
        sv = self.sv
        s = ttk.Style()
        tn = s.theme_names()
        i = tn.index(s.theme.name) # 初始索引值：morph主题为 9
        # print(i)

        b = ttk.Button(f, text='关于', command=self.fun)
        l = ttk.Label(f, text='主题')
        self.tm = ttk.Combobox(f, width=15, values=tn, textvariable=sv)
        self.tm.current(i) # 初始主题
        b2 = ttk.Button(f, text='应用', command=self.fun2)

        b.pack(side=LEFT, padx=(0,10))
        b2.pack(side=RIGHT, padx=(10,0))
        self.tm.pack(side=RIGHT, padx=(10,0))
        l.pack(side=RIGHT, padx=(10,0))
    def row2(self):
        '''日志栏'''
        lf = self.lf
        sv = self.sv2

        l = ttk.Label(lf, text='路径')
        e = ttk.Entry(lf, width=40, textvariable=sv)
        b = ttk.Button(lf, text='浏览', width=10, command=self.fun3)

        l.pack(side=LEFT, padx=10)
        e.pack(side=LEFT, padx=10, fill=X, expand=YES)
        b.pack(side=LEFT, padx=10)
    def row3(self):
        '''信号栏'''
        lf = self.lf2
        iv = self.iv
        iv2 = self.iv2
        iv3 = self.iv3
        iv4 = self.iv4

        cb = ttk.Checkbutton(lf,text='17F', variable=iv, onvalue=1, offvalue=0)
        cb2 = ttk.Checkbutton(lf,text='31B', variable=iv2, onvalue=1, offvalue=0)
        cb3 = ttk.Checkbutton(lf,text='146', variable=iv3, onvalue=1, offvalue=0)
        cb4 = ttk.Checkbutton(lf, text='REL', variable=iv4, onvalue=1, offvalue=0)

        cb.pack(side=LEFT, padx=10)
        cb2.pack(side=LEFT, padx=10)
        cb3.pack(side=LEFT, padx=10)
        cb4.pack(side=LEFT, padx=10)
    def row4(self):
        '''操作栏'''
        lf = self.lf3

        self.b = ttk.Button(lf, text='生成csv', command=self.fun4)
        self.pb = ttk.Progressbar(lf, maximum=100, bootstyle='success-striped')

        self.b.pack(padx=10, fill=X, expand=YES)
        self.pb.pack(padx=10, fill=X, expand=YES)

    def fun(self):
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
    def fun2(self):
        '''应用主题'''
        s = ttk.Style()
        cb = self.tm.get()

        s.theme_use(cb)
        print(f'应用主题:{cb}')
    def fun3(self):
        '''浏览文件'''
        sv = self.sv2
        path = filedialog.askopenfilename(title='选择日志文件')
        if path:
            sv.set(path)
    def fun4(self):
        '''生成csv'''
        t, t2, t3, t4, t5, t6 = self.sv.get(), self.sv2.get(), self.iv.get(), self.iv2.get(), self.iv3.get(), self.iv4.get()
        f = self.fun5
        pb = self.pb # 进度条
        b = self.b # 按钮

        print(f'当前设定:\n主题:{t}\n路径:{t2}\n17F:{t3}\n31B:{t4}\n146:{t5}\nrel:{t6}\n')

        # 创建cache文件夹
        if not pa.exists('cache'):
            mkdir('cache')

        # 过滤数据
        fl.log_0011(t2),f(1,10,'筛选0011数据中...')

        # 创建csv文件夹
        if not pa.exists('csv'):
            mkdir('csv')

        # 输出
        if t3 == 1:
            fl.log_17F(),f(10,25,'17F数据处理中...')
            u17F.csv(),f(26,40,'17F数据生成中...')
        if t4 == 1:
            fl.log_31B(),f(41,45,'31B数据处理中...')
            u31B.csv(),f(46,50,'31B数据生成中...')
        if t5 == 1:
            fl.log_146(),f(51,70,'146数据处理中...')
            u146.csv(),f(71,90,'146生成处理中...')

        if t6 == 1:
            if not pa.exists('cache/log_17F.txt'):
                fl.log_17F(), f(10, 25, '17F数据处理中...')
                u17F.csv(), f(26, 40, '17F数据生成中...')
            if not pa.exists('cache/log_146.txt'):
                fl.log_146(), f(51, 70, '146数据处理中...')
                u146.csv(), f(71, 90, '146生成处理中...')
            fl.log_rel()
            rel.csv()

        f(91,99,'csv文件生成中...')

        pb['value'] = 100
        b['text'] = 'csv文件已生成^-^'

        # 弹窗提示
        showinfo('(*^▽^*) Yeah~','csv文件已生成在根目录')
        b.config(state=NORMAL)

        # 初始化进度条
        pb['value'] = 0
        b['text'] = '生成csv'
    def fun5(self, i, j, l):
        '''进度更新'''
        pb = self.pb # 进度条
        b = self.b # 按钮
        j = j + 2
        for k in range(i,j):
            pb['value'] = k  # 修改进度
            pb.update()
            b['text'] = f'进度:{k}% {l}' # 修改按钮文本
            sleep(0.02)
    def fun6(self, a):
        '''拖入读取'''
        sv = self.sv2
        p = '\n'.join((item.decode('gbk') for item in a))
        sv.set(p)

if __name__ == '__main__':
    w = ttk.Window('----------调试窗口----------','litera')
    w.geometry('+640+340')
    app(w)
    l = ttk.Label(text='----------版本：Demo----------')
    l.pack(side=RIGHT, padx=10)
    w.mainloop()
