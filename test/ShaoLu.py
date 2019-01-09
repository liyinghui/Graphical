# -*- coding:utf-8 -*-

from Tkinter import *
from ttk import *
from time import sleep
import random
import os
import subprocess


class LoginWindow():
    def __init__(self):
        self.top = Tk()
        self.top.title('Doctor音箱烧录工具1.0')
        self.top.geometry("600x550")
        self.top.resizable(0, 0)
        self.top.iconbitmap('./imgs/favicon.ico')

        self.setup_ui()

        self.entry_list = []
        self.file_path = './sn.txt'
        self.file_list = []

        self.load_file_info()

    # 界面循环
    def show(self):
        self.top.mainloop()

    # 设置界面
    def setup_ui(self):
        # 实例化样式
        self.style_01 = Style()
        # 默认情况下，所有label标签都遵循此样式，除非按style单独指定 , background="LightBlue"
        self.style_01.configure("left.TPanedwindow", background="LightBlue")
        # 实例化面板，添加左面板
        self.left_window = PanedWindow(width=350, height=560, style="left.TPanedwindow")
        self.left_window.pack(side=LEFT,  padx=20, pady=10)
        # 实例化控件，在面板上添加控件
        self.left_label_01 = Label(self.left_window, text='SN       ')
        self.left_label_01.place(x=20, y=10)
        self.left_label_02 = Label(self.left_window, text='WIFI Mac')
        self.left_label_02.place(x=20, y=50)
        self.left_label_03 = Label(self.left_window, text='BT  Mac')
        self.left_label_03.place(x=20, y=90)
        self.left_label_04 = Label(self.left_window, text='FLAG     ')
        self.left_label_04.place(x=20, y=130)
        self.left_label_05 = Label(self.left_window, text='KEY      ')
        self.left_label_05.place(x=20, y=170)

        self.left_entry_01 = Entry(self.left_window)
        self.left_entry_01.place(x=100, y=10)
        # self.left_entry_01.insert(INSERT, 'SA03212185045706')
        self.left_entry_02 = Entry(self.left_window)
        self.left_entry_02.place(x=100, y=50)
        self.left_entry_03 = Entry(self.left_window)
        self.left_entry_03.place(x=100, y=90)
        self.left_entry_04 = Entry(self.left_window)
        self.left_entry_04.place(x=100, y=130)
        self.left_entry_05 = Entry(self.left_window)
        self.left_entry_05.place(x=100, y=170)
        self.left_text_01 = Text(self.left_window,  width=33, height=20)
        self.left_text_01.place(x=20, y=220)

        # button按钮点击后调用函数，获取输入框值
        self.left_button_01 = Button(self.left_window, text='开始烧录', command=lambda: self.get_entry())
        self.left_button_01.place(x=20, y=500)
        self.left_button_02 = Button(self.left_window, text='清空内容', command=lambda: self.clear_text_info())
        self.left_button_02.place(x=120, y=500)
        self.left_button_03 = Button(self.left_window, text='重新加载', command=lambda: self.reload_file_info())
        self.left_button_03.place(x=220, y=500)
        # 实例化面板，右面板
        # pack()方法要单独一行调用，才能在面板上添加控件；
        self.right_window = PanedWindow(width=200, height=560, style="left.TPanedwindow")
        self.right_window.pack(side=RIGHT,  padx=20, pady=10)
        self.right_label_02 = Label(self.right_window, text=' 日志管理 ')
        self.right_label_02.place(x=60, y=10)
        self.right_button_03 = Button(self.right_window, text='添加日志', command=lambda: self.add_log())
        self.right_button_03.place(x=60, y=50)
        self.right_button_04 = Button(self.right_window, text='打印日志', command=lambda: self.print_log())
        self.right_button_04.place(x=60, y=90)
        self.right_button_05 = Button(self.right_window, text='导出日志', command=lambda: self.pull_log())
        self.right_button_05.place(x=60, y=130)
        self.right_button_06 = Button(self.right_window, text='删除日志', command=lambda: self.rm_log())
        self.right_button_06.place(x=60, y=170)

    # 定义函数获得entry输入值
    def get_entry(self):
        print (self.left_entry_01.get())
        print (self.left_entry_02.get())
        print (self.left_entry_03.get())
        print (self.left_entry_04.get())
        print (self.left_entry_05.get())
        entry_list = []
        for left_entry in [self.left_entry_01.get(), self.left_entry_02.get(), self.left_entry_03.get(), self.left_entry_04.get(), self.left_entry_05.get()]:
            entry_list.append(left_entry)

        self.left_text_01.insert(INSERT, entry_list)
        self.push_alpha_migu_sn()

        # num = random.randint(1, 3)
        # if num == 3:
        #     self.left_text_01.insert(INSERT, '烧录成功')
        # else:
        #     self.left_text_01.insert(INSERT, "烧录失败")
        # return entry_list

    # 清空text内容
    def clear_text_info(self):
        self.left_text_01.delete(1.0, 2.0)
        self.left_entry_01.delete(0, END)
        self.left_entry_02.delete(0, END)
        self.left_entry_03.delete(0, END)
        self.left_entry_04.delete(0, END)
        self.left_entry_05.delete(0, END)

    # 加载配置文件
    def load_file_info(self):
        fo = open(self.file_path, 'r')
        # 读取第一行
        current_line = fo.readline()
        # 如果current_line不是空
        while current_line:
            temp_list = current_line
            self.file_list.append(temp_list)
            # 读取下一行
            current_line = fo.readline()

        sn = str(self.file_list[0][3:]).strip()
        wifi = str(self.file_list[1][9:]).strip()
        bt = str(self.file_list[2][8:]).strip()
        flag = str(self.file_list[3][5:]).strip()
        key = str(self.file_list[4][4:]).strip()

        self.left_entry_01.insert(INSERT, sn)
        self.left_entry_02.insert(INSERT, wifi)
        self.left_entry_03.insert(INSERT, bt)
        self.left_entry_04.insert(INSERT, flag)
        self.left_entry_05.insert(INSERT, key)

        # 加载配置文件

    def reload_file_info(self):
        fo = open('./sn.txt', 'r')
        file_list = []
        # 读取第一行
        current_line = fo.readline()
        # 如果current_line不是空
        while current_line:
            temp_list = current_line
            file_list.append(temp_list)
            # 读取下一行
            current_line = fo.readline()

        sn = str(file_list[0][3:]).strip()
        print sn
        wifi = str(file_list[1][9:]).strip()
        bt = str(file_list[2][8:]).strip()
        flag = str(file_list[3][5:]).strip()
        key = str(file_list[4][4:]).strip()

        self.left_entry_01.insert(INSERT, sn)
        self.left_entry_02.insert(INSERT, wifi)
        self.left_entry_03.insert(INSERT, bt)
        self.left_entry_04.insert(INSERT, flag)
        self.left_entry_05.insert(INSERT, key)

    # 导入配置文件，功能相当于烧录SN
    def push_alpha_migu_sn(self):
        bin_file = './nvram_helper.bin'
        file_path = os.path.abspath(bin_file)
        # Import SN and other information to the speaker, which is equivalent to automatic networking
        touch = 'adb shell touch /data/dingdong/etc/log.txt'
        nvram_helper = 'adb push '+file_path + ' /tmp'
        chmod = 'adb shell chmod 777 tmp/nvram_helper.bin'
        psn = 'adb shell /tmp/nvram_helper.bin -w ' + self.left_entry_01.get() + ',' + self.left_entry_02.get() + ',' + self.left_entry_03.get() + ',' + self.left_entry_04.get() + ',' + self.left_entry_05.get()
        async = 'adb shell sync'
        areboot = 'adb shell reboot'

        for s in [touch, nvram_helper, chmod, psn, async, areboot]:
            print(s)
            try:
                ps = subprocess.Popen(s, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            except IOError:
                print('Error:')
            sleep(1)
            print(ps.stdout.readlines())
            out = ps.stdout.readlines()
            self.left_text_01.insert(INSERT, out)

    def add_log(self):
        os.system('start .\\1addDingdonglog.bat')

    def print_log(self):
        os.system('start .\\2printDingdongLog.bat')

    def pull_log(self):
        os.system('start .\\3getDingdongLog.bat')

    def rm_log(self):
        os.system('start .\\4rmDingdonglog.bat')


if __name__ == '__main__':
    app = LoginWindow()
    app.show()

    # app = LoginWindow()
    # app.get_entry()
    # app.push_alpha_migu_sn()


