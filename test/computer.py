
# -*- coding:utf-8 -*-

# 创建一个三窗格
from Tkinter import *

root = Tk()

# 计算机窗口大小  （宽x高）
root.geometry("250x380")

# 设置计算机title
root.title("计算器")

# Frame就是在屏幕上的一块矩形区域  多用来作为容器使用
frame_show = Frame(width=250, height=150, bg='#ddd')

# 添加到主窗体
frame_show.pack()

# 主窗体

# 实例化一个产生变量的类
v = StringVar()
# 初始化赋值'0'
v.set('0')
# Lable(用于存放父组件，属性参数   )
# anchor  文本相对于标签中心的位置   默认是center N S W E
show_label = Label(frame_show, textvariable=v, bg='white', width='30', height='1', anchor='e', font=("黑体", 20, "bold"))

# 添加到主窗体
show_label.pack(padx=10, pady=10)

frame_bord = Frame(width=250, height=350, bg='#ccc')
frame_bord.pack(padx=10, pady=10)

calc = []
isoperate = False


def change(num):
    global isoperate
    if isoperate == False:
        if v.get() == "0" and num == '.':
            v.set(length(v.get() + num))
        elif v.get() == "0":
            v.set(length(num))
        else:
            if num == ".":
                if v.get().count(".") < 1:
                    v.set(v.get() + num)
            else:
                v.set(v.get() + num)
    else:
        v.set(length(num))
        isoperate = False


# 检验字符串的长度的函数
def length(str):
    if len(str) > 12:
        return str[0:12]
    else:
        return str


# 清空函数
def clear():
    global calc
    calc = []
    # 屏幕窗口恢复到0
    v.set("0")


# 操作 +  -  *  /
def operate(sign):
    global calc
    global isoperate
    isoperate = True
    calc.append(v.get())
    if sign == "+":
        calc.append(sign)
    elif sign == "-":
        calc.append(sign)
    elif sign == "*":
        calc.append(sign)
    elif sign == "/":
        calc.append(sign)


# 运算
global calcstr


def equal():
    global calc
    # 获取当前界面的值
    calc.append(v.get())
    print(calc)
    # 列表变字符串 join 把列表用什么拼接成字符串
    calcstr = "".join(calc)
    print(calcstr)
    print(type(calcstr))

    # 运算操作 eval（）把str当成有效的表达式进行计算
    result = eval(calcstr)
    if len(str(result)) > 12:
        result = str(result)
        result = result[0:12]
        v.set(result)
    else:
        v.set(result)

    print(result)


# 定义退格函数
def delete():
    # 获取v.get（）长度
    num = len(v.get())
    # 如果长度>1 怎么办
    if num > 1:
        strnum = v.get()
        strnum = strnum[0:num - 1]
        v.set(strnum)
    # 小于等于1的时候
    else:
        v.set("0")


# 正负操作
def fan():
    strnum = v.get()
    if strnum[0] == '-':
        v.set(strnum[1:])
    elif strnum[0] != '-' and strnum != '0':
        v.set('-' + strnum)


# Button(父组件，属性参数)
button_del = Button(frame_bord, text='←', width='5', height='1', command=lambda: delete()).grid(row='1', column='0')
button_del = Button(frame_bord, text='CE', width='5', height='1', command=lambda: clear()).grid(row='1', column='1')
button_del = Button(frame_bord, text='C', width='5', height='1', command=lambda: clear()).grid(row='1', column='2')
button_del = Button(frame_bord, text='±', width='5', height='1', command=lambda: fan()).grid(row='1', column='3')

button_del = Button(frame_bord, text='7', width='5', height='1', command=lambda: change("7")).grid(row='2', column='0')
button_del = Button(frame_bord, text='8', width='5', height='1', command=lambda: change("8")).grid(row='2', column='1')
button_del = Button(frame_bord, text='9', width='5', height='1', command=lambda: change("9")).grid(row='2', column='2')
button_del = Button(frame_bord, text='/', width='5', height='1', command=lambda: operate("/")).grid(row='2', column='3')

button_del = Button(frame_bord, text='4', width='5', height='1', command=lambda: change("4")).grid(row='3', column='0')
button_del = Button(frame_bord, text='5', width='5', height='1', command=lambda: change("5")).grid(row='3', column='1')
button_del = Button(frame_bord, text='6', width='5', height='1', command=lambda: change("6")).grid(row='3', column='2')
button_del = Button(frame_bord, text='-', width='5', height='1', command=lambda: operate("-")).grid(row='3', column='3')

button_del = Button(frame_bord, text='1', width='5', height='1', command=lambda: change("1")).grid(row='4', column='0')
button_del = Button(frame_bord, text='2', width='5', height='1', command=lambda: change("2")).grid(row='4', column='1')
button_del = Button(frame_bord, text='3', width='5', height='1', command=lambda: change("3")).grid(row='4', column='2')
button_del = Button(frame_bord, text='*', width='5', height='1', command=lambda: operate("*")).grid(row='4', column='3')

button_del = Button(frame_bord, text='0', width='5', height='1', command=lambda: change("0")).grid(row='5', column='0')
button_del = Button(frame_bord, text='.', width='5', height='1', command=lambda: change(".")).grid(row='5', column='1')
button_del = Button(frame_bord, text='+', width='5', height='1', command=lambda: operate("+")).grid(row='5', column='2')
button_del = Button(frame_bord, text='=', width='5', height='1', command=lambda: equal()).grid(row='5', column='3')

root.mainloop()
