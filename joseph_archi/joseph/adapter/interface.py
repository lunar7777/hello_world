# https://blog.csdn.net/hong2511/article/details/81741509
from tkinter import *
#import easygui
from joseph.use_case.start_game import start_game
import os
from tkinter import filedialog
#from joseph.adapter.reader import load_data

def interface():
    master = Tk()
    master.title("约瑟夫环")  # 窗口标题
    frame = Frame(master)  # 确定一个框架 

    frame.pack(padx=22, pady=22)  # 与边框的边距

    v1 = StringVar()  # 用于存储输入的数据
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()

    def test(content):
        return content.isdigit()


    testCMD = frame.register(test)  # 将函数进行包装

    # window_setting
    Label(frame, text="startnum", padx=10).grid(row=0, column=0)
    e1 = Entry(
        frame, width=10, textvariable=v1, validate="key", validatecommand=(test, "%p")
    ).grid(
        row=0, column=1, pady=10
    )  # %p 是输入框的最新内容 . 当输入框允许改变的时候该值有效 ,

    Label(frame, text="step", padx=10).grid(row=1, column=0)
    e2 = Entry(
        frame, width=10, textvariable=v2, validate="key", validatecommand=(test, "%p")
    ).grid(
        row=1, column=1, pady=15
    )  # textvariable是文本框的值，是一个StringVar()对象

    Label(frame, text="survival", padx=10).grid(row=2, column=0)
    e3 = Entry(frame, width=23, textvariable=v3, state="readonly").grid(row=2, column=1)

    #Label(frame,text="选择文件", padx=10).grid(row=3,column=0)
    #e4 = Entry(frame,width=10,textvariable=v4, state="readonly").grid(row=3,column=1)

    def call():  # 调用函数
        result = start_game(int(v1.get()), int(v2.get()))
        v3.set(result)

    #def choose_file():
    #    filepath =  filedialog.askopenfilename()  # 弹出窗口以选择文件
    #    aka = load_data(filepath)
    #    v4.set(aka)

    Button(frame, text="Run", command=call).grid(row=1, column=2, pady=5)
#    Button(frame, text="选择文件", command=choose_file).grid(row=3,column=2,pady=5)

