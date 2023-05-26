# -*- coding: utf-8 -*-
# @Time ： 2023/5/25 10:18
# @Auth ： JeremyChim
# @File ：app.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import ui.win as ui
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

w = ttk.Window('以太网报文解析工具','morph')
w.geometry('+640+240')
ui.app(w)
l = ttk.Label(text='版本：v1.00')
l.pack(side=RIGHT, padx=10)
w.mainloop()