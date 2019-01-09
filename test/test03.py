# -*- coding:utf-8 -*-

from Tkinter import *
from ttk import *


class LoginWindow():
    def __init__(self):
        self.top = Tk()
        self.top.title('title')
        self.top.geometry("600x600")

        self.setup_ui()

        # self.show()

    def setup_ui(self):
        self.style_01 = Style()
        # 默认情况下，所有label标签都遵循此样式，除非按style单独指定 , background="LightBlue"
        self.style_01.configure("left.TPanedwindow", background="LightBlue")

        self.left_window = PanedWindow(width=300, height=560, style="left.TPanedwindow")
        self.left_window.pack(side=LEFT,  padx=20, pady=10)
        self.left_label_01 = Label(self.left_window, text='SN   ')
        self.left_label_01.place(x=20, y=10)
        self.left_label_02 = Label(self.left_window, text='WIFI MAC')
        self.left_label_02.place(x=20, y=50)
        self.left_label_03 = Label(self.left_window, text='BT MAC')
        self.left_label_03.place(x=20, y=90)
        self.left_label_04 = Label(self.left_window, text='FLAG  ')
        self.left_label_04.place(x=20, y=130)
        self.left_label_05 = Label(self.left_window, text='KEY   ')
        self.left_label_05.place(x=20, y=170)

        self.left_entry_01 = Entry(self.left_window)
        self.left_entry_01.place(x=100, y=10)
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

        self.left_button_01 = Button(self.left_window, text='开始')
        self.left_button_01.place(x=20, y=500)

        # pack()方法要单独一行调用
        self.right_window = PanedWindow(width=200, height=200, style="left.TPanedwindow")
        self.right_window.pack(side=RIGHT,  padx=20, pady=10)
        self.right_label_02 = Label(self.right_window, text='lable02 pane')
        self.right_label_02.place(x=20, y=10)
        #
        # lable03 = Label(self.right_window, text='lable03 pane')
        # self.right_window.add(lable03)

    def show(self):
        self.top.mainloop()


if __name__ == '__main__':
    app = LoginWindow()
    app.show()
