# -*- coding:utf-8 -*-
from tkinter import *
# from tkinter.simpledialog import *
import os
import time
from datetime import datetime
import shutil


def show_entry_fields():
    global usb_path, save_path
    usb_path = e1.get()
    save_path = e2.get()
    root.destroy()


root = Tk()
root.title('usb copy 0.1')
Label(root, text="请输入U盘盘符地址").grid(row=0)
Label(root, text="请输入保存地址").grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e1.insert(0, "E:/")
e2.insert(0, "D:/haha")
Button(root, text='OK', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
root.mainloop()

# usb_path = askstring(title='string', prompt='请输入U盘盘符地址，如小括号内 (E:/)：')
# save_path = askstring(title='string', prompt='请输复制后存储的地址，如小括号内 (D:/haha)：')
# root.withdraw()  # 隐藏窗口
# root.mainloop()  # 消息循环


while (True):
    if os.path.exists(usb_path):
        shutil.copytree(usb_path, os.path.join(save_path, datetime.now().strftime("%Y%m%d_%H%M%S")))
        break
    else:
        time.sleep(10)
