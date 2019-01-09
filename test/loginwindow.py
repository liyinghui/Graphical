# -*- coding:utf-8 -*-

from Tkinter import *
from ttk import *


class LoginWindow():
    def __init__(self):
        self.top = Tk()
        self.top.title('title')
        # self.top.geometry("400x300")

        self.setup_ui()

        self.show()

    def setup_ui(self):
        m = Frame()
        m.pack()
        lef = Label(text='label')
        lef.pack()
        # m1 = PanedWindow()  # 默认是左右分布的
        # m1.pack(fill=BOTH, expand=1)
        # left = Label(m1, text='left pane')
        # m1.add(left)
        #
        # m2 = PanedWindow(orient=VERTICAL)
        # m1.add(m2)
        # top = Label(m2, text='top pane')
        # m2.add(top)
        #
        # bottom = Label(m2, text='bottom pane')
        # m2.add(bottom)

        # self.left_window = PanedWindow()
        # self.left_window.pack(fill=BOTH, expand=1)
        # lable01 = Label(self.left_window, text='lable01 pane')
        # self.left_window.add(lable01)
        #
        # self.right_window = PanedWindow(orient=VERTICAL)
        # self.left_window.add(self.right_window)
        # lable02 = Label(self.right_window, text='lable02 pane')
        # self.right_window.add(lable02)
        #
        # lable03 = Label(self.right_window, text='lable03 pane')
        # self.right_window.add(lable03)

    def show(self):
        self.top.mainloop()


if __name__ == '__main__':
    app = LoginWindow()
    app.show()
