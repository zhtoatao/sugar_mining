import time
import re
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font, BOLD
import threading
from module import chushi,mining
from core import image,log_creater
import os




###################################################################################################################################################
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
###################################################################################################################################################

def main():
    chushi.delet()
    chushi.start_to_home()
    mining.mining()
    mining.result_saver()
    mining.sort_result()


while True:
    address_ = input("要挖的vh 写数字或者地图名称: ")
    found = False
    for pattern, value in mining.address.items():
        if re.fullmatch(pattern, address_):
            mining.vh = value
            log_message = log_creater.write_log(f"将要挖这个地图: {mining.vh}")
            print(log_message)
            found = True
            break
    if not found:
        log_message = log_creater.write_log("没有这个图捏")
        print(log_message)
    break

while True:
    main()
    log_message = log_creater.write_log(f"\n现在的运行情况:\n准备进行n级第{mining.n}-{mining.n_}关的挖矿\n准备进行h级第{mining.h}-{mining.h_}关的挖矿\nn级地图还差{150-(mining.n-1)*10-mining.n_+1}没挖\nh级地图还差{150-(mining.h-1)*10-mining.h_+1}没挖\nvh级地图还差{10-mining.vh_+1}没挖")
    print(log_message)
    if mining.h == 16:
        log_message = log_creater.write_log(f"\n全部挖完了，请前往result文件夹查看挖矿结果")
        print(log_message)
        break