# -*- coding: utf-8 -*-
# @Time ： 2023/5/25 10:18
# @Auth ： JeremyChim
# @File ：app.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import ui.win as ui
from ttkbootstrap import Window
from ttkbootstrap import Label
from ttkbootstrap.constants import RIGHT

w = Window('以太网报文解析工具','journal')
w.geometry('+640+340')
ui.app(w)
l = Label(text='版本：v2.10')
l.pack(side=RIGHT, padx=10)
w.mainloop()