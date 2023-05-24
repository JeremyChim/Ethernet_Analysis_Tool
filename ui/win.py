# -*- coding: utf-8 -*-
# @Time ： 2023/5/24 15:50
# @Auth ： JeremyChim
# @File ：win.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

# 外部函数调用
from ttkbootstrap.constants import *
from tkinter import filedialog
import ttkbootstrap as ttk
import tkinter as tk
import pathlib
import os

# 自定义函数调用
import func.flier as fl
import func.udp146 as u146
import func.udp17F as u17F
import func.udp31B as u31B

# 类
class app(ttk.Frame):
    def __init__(self, win):
        super().__init__(win) # app = ttk.Frame(win)
        self.pack() # app.pack()

        # 获取路径
        self.path = pathlib.Path().absolute().as_posix()
        path = self.path

        # 容器
        self.sv = ttk.StringVar() # 主题名
        self.sv2 = ttk.StringVar(value=path) # log路径
        self.iv = ttk.IntVar(value=1) # 17F
        self.iv2 = ttk.IntVar(value=1) # 31B
        self.iv3 = ttk.IntVar(value=1) # 146

        # 外框
        f = ttk.Frame(padding=10)
        f.pack(fill=X, expand=YES, anchor=N)

        # 内框
        self.f2 = ttk.Frame(f, padding=10)
        self.lf = ttk.LabelFrame(f, text='日志', padding=10)
        self.lf2 = ttk.LabelFrame(f, text='信号', padding=10)
        self.lf3 = ttk.LabelFrame(f, text='操作', padding=10)

        self.f2.pack(fill=X, expand=YES)
        self.lf.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf2.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf3.pack(fill=X, expand=YES)

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
        i = tn.index(s.theme.name) # 初始索引值：pulse主题为 7
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

        cb = ttk.Checkbutton(lf,text='17F', variable=iv, onvalue=1, offvalue=0)
        cb2 = ttk.Checkbutton(lf,text='31B', variable=iv2, onvalue=1, offvalue=0)
        cb3 = ttk.Checkbutton(lf,text='146', variable=iv3, onvalue=1, offvalue=0)

        cb.pack(side=LEFT, padx=10)
        cb2.pack(side=LEFT, padx=10)
        cb3.pack(side=LEFT, padx=10)
    def row4(self):
        '''操作栏'''
        lf = self.lf3

        b = ttk.Button(lf, text='生成csv', command=self.fun4)
        b.pack(side=LEFT, padx=10, fill=X, expand=YES)

    def fun(self):
        '''关于'''
        tk.messagebox.showinfo('关于 以太网报文解析工具',
                               '作者：Jer小铭😎 \n'
                               '技术支持：Mavis🤣 \n'
                               '建议提供：少基同学🤪 \n'
                               '思路提供：家文同学😏 \n'
                               '测试验证：少丽同学🤨 \n'
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
        t = self.sv.get()
        t2 = self.sv2.get()
        t3 = self.iv.get()
        t4 = self.iv2.get()
        t5 = self.iv3.get()

        print('---当前设定---')
        print(f'主题:{t}')
        print(f'路径:{t2}')
        print(f'17F:{t3}')
        print(f'31B:{t4}')
        print(f'146:{t5}')

if __name__ == '__main__':
    w = ttk.Window('以太网报文解析工具','pulse')
    w.geometry('+640+240')
    app(w)
    l = ttk.Label(text='版本：v0.00')
    l.pack(side=RIGHT, padx=10)
    w.mainloop()
