import pathlib
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
# import threading

class MapDrawTool(ttk.Frame):
    '''该class是地图打点工具的内部框架布局'''

    def __init__(self, master):
        super().__init__(master, padding=15)
        self.pack(fill=BOTH, expand=YES)

        _path = pathlib.Path().absolute().as_posix()
        self.path_var = ttk.StringVar(value=_path)
        # self.draw_progress_var = ttk.StringVar(value=0)

        self.menu_row = ttk.Frame(self)
        self.menu_row.pack(fill=X, expand=YES, pady=(0,15))

        file_text = '日志'
        self.file_lf = ttk.Labelframe(self, text=file_text, padding=15)
        self.file_lf.pack(fill=X, expand=YES, anchor=N)

        draw_text = '转译'
        self.draw_lf = ttk.Labelframe(self, text=draw_text, padding=15)
        self.draw_lf.pack(fill=X, expand=YES, anchor=N, pady=(15,0))

        self.create_menu_row()
        self.create_path_row()
        self.create_key_row()
        self.create_draw_row()

    def create_menu_row(self):
        '''创建一个菜单行'''
        _style = ttk.Style()
        _theme_name = _style.theme_names()

        about_btn = ttk.Button(
            master=self.menu_row,
            text='关于',
            command=self.about,
            width=8,
            bootstyle=OUTLINE
        )
        about_btn.pack(side=LEFT)

        theme_lbl = ttk.Label(master=self.menu_row,
                        text='主题：')

        self.theme_cb = ttk.Combobox(master=self.menu_row,
                               values=_theme_name,
                               width=10)

        theme_btn = ttk.Button(master=self.menu_row,
                         text='应用',
                         command=self.change_theme
                         )

        theme_btn.pack(side=RIGHT, padx=5)
        self.theme_cb.pack(side=RIGHT)
        theme_lbl.pack(side=RIGHT)

        self.theme_cb.current(_theme_name.index(_style.theme.name)) # 将初始主题名索引

    def create_path_row(self):
        '''该def是path路径行的框架布局'''
        path_row = ttk.Frame(self.file_lf)
        path_row.pack(fill=X, expand=YES)
        path_lbl = ttk.Label(path_row, text='路径', width=8)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        path_ent = ttk.Entry(path_row, textvariable=self.path_var)
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        browse_btn = ttk.Button(
            master=path_row,
            text='浏览',
            command=self.on_browse,
            width=8,
            # bootstyle=OUTLINE
        )
        browse_btn.pack(side=LEFT, padx=5)

    def create_key_row(self):
        key_row = ttk.Frame(self.file_lf)
        key_row.pack(fill=X, expand=YES, pady=(15, 0))

        key_lbl = ttk.Label(key_row, text='关键字')
        key_lbl.pack(side=LEFT, padx=15)

        cb1 = ttk.Checkbutton(key_row, text='17F')
        cb1.pack(side=LEFT, padx=15)

        cb2 = ttk.Checkbutton(key_row, text='31B')
        cb2.pack(side=LEFT, padx=15)

        cb3 = ttk.Checkbutton(key_row, text='146')
        cb3.pack(side=LEFT, padx=15)

    def create_draw_row(self):
        '''将draw行添加至标签框架'''
        draw_row = ttk.Frame(self.draw_lf)
        draw_row.pack(fill=X, expand=YES)
        draw_pgb_row = ttk.Frame(self.draw_lf)
        draw_pgb_row.pack(fill=X, expand=YES)

        draw_btn = ttk.Button(
            master=draw_row,
            text='生成csv',
            width=70,
            # bootstyle=DANGER
            bootstyle=(DANGER,OUTLINE)
        )

        # self.draw_pgb = ttk.Progressbar(
        #     master=draw_pgb_row,
        #     bootstyle='success-striped',
        #     orient='horizontal',
        #     mode='determinate',
        #     maximum = 1,
        #     value = self.draw_progress_var.get()
        # )
        #
        # # self.draw_pgb.start()    #进度条动动看
        # export_excel_btn.pack(side=LEFT, expand=YES, padx=0, fill=X)
        draw_btn.pack(side=LEFT, expand=YES, padx=0, fill=X)
        # self.draw_pgb.pack(fill=X)

    def on_browse(self):
        '''打开文件浏览器，并输出选中的文件路径'''
        path = filedialog.askopenfilename(title='选择日志文件')
        if path:
            self.path_var.set(path)

    def about(self):
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

    # def update_progress(self, locations):
    #     for i in range(1, len(locations) + 1, 10):
    #         self.draw_pgb['value'] = i / len(locations)
    #         self.draw_pgb.update()

    def change_theme(self):
        '''获取theme_cb的值（主题名），并应用主题'''
        print(f'正在应用主题：{self.theme_cb.get()}')
        t = self.theme_cb.get()
        ttk.Style().theme_use(t)

if __name__ == '__main__':

    app = ttk.Window('以太网报文解析工具', 'litera')
    MapDrawTool(app)
    version = ttk.Label(app, text='版本：v0.00')
    version.pack(side=RIGHT, padx=15)
    app.place_window_center()    #让显现出的窗口居中
    # app.resizable(False,False)   #让窗口不可更改大小
    app.mainloop()