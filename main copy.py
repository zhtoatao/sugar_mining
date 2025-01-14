import time
import re
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font, BOLD
import threading
from module import click_app,chushi
from core import image,log_creater
import os


image_list = [f"n{i}o.png" for i in range(1, 17)]
c_tansuoquan_list = []
c_saodangquan_list = []
c_tiliyao_list = []
b_jiajvbi_list = []
b_srquan_list = []
b_jinbi_list = []
a_zhuanwu_list = []
a_ssrquan_list = []
s_xingtangshi_list = []
address = {
    r'スラートキーの氷山': 1,
    r'ドースィー西部': 2,
    r'ドースィーの山麓': 3,
    r'デセールの王城付近': 4,
    r'デセール湾港': 5,
    r'隠された都市': 6,
    r'ヘルゥ北部': 7,
    r'ヘルゥ南部': 8,
    r'メアオノの中心部': 9,
    r'マケア南西の沿岸': 10,
    r'マケア南東の森林地帯': 11,
    r'カンロ南部': 12,
    r'トルテ南部の街道付近': 13,
    r'トルテの都市近郊': 14,
    r'トルテ東部の三日月島': 15,
    r'1': 1,
    r'2': 2,
    r'3': 3,
    r'4': 4,
    r'5': 5,
    r'6': 6,
    r'7': 7,
    r'8': 8,
    r'9': 9,
    r'10': 10,
    r'11': 11,
    r'12': 12,
    r'13': 13,
    r'14': 14,
    r'15': 15
}




n = 16
n_ = 1
h = 15
h_ = 8
vh = 1
vh_ = 1
address_ = None

###################################################################################################################################################
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
###################################################################################################################################################

def sorting(level, number, level_name):
    while True:
        if image.co("failure.png", False):
            log_message = log_creater.write_log(f"{level_name} {level}-{number} 什么都没有")
            print(log_message)
            break
        if image.co("c_tansuoquan.png", False, 1, 0.98):
            log_message = log_creater.write_log(f"成功找到c-探索券！位置在 {level_name} {level}-{number}")
            print(log_message)
            c_tansuoquan_list.append((level_name, level, number))
            break
        if image.co("c_saodangquan.png", False, 1, 0.98):
            log_message = log_creater.write_log(f"成功找到c-扫荡券！位置在 {level_name} {level}-{number}")
            print(log_message)
            c_saodangquan_list.append((level_name, level, number))
            break
        if image.co("c_tiliyao.png", False):
            log_message = log_creater.write_log(f"成功找到c-体力药！位置在 {level_name} {level}-{number}")
            print(log_message)
            c_tiliyao_list.append((level_name, level, number))
            break
        if image.co("b_jiajvbi.png", False):
            log_message = log_creater.write_log(f"成功找到b-家具币！位置在 {level_name} {level}-{number}")
            print(log_message)
            b_jiajvbi_list.append((level_name, level, number))
            break
        if image.co("b_srquan.png", False):
            log_message = log_creater.write_log(f"成功找到b-sr券！位置在 {level_name} {level}-{number}")
            print(log_message)
            b_srquan_list.append((level_name, level, number))
            break
        if image.co("b_jinbi.png", False):
            log_message = log_creater.write_log(f"成功找到b-金币！位置在 {level_name} {level}-{number}")
            print(log_message)
            b_jinbi_list.append((level_name, level, number))
            break
        if image.co("a_zhuanwu.png", False):
            log_message = log_creater.write_log(f"成功找到a-专武！位置在 {level_name} {level}-{number}")
            print(log_message)
            a_zhuanwu_list.append((level_name, level, number))
            break
        if image.co("a_ssrquan.png", False):
            log_message = log_creater.write_log(f"成功找到a-ssr券！位置在 {level_name} {level}-{number}")
            print(log_message)
            a_ssrquan_list.append((level_name, level, number))
            break
        if image.co("s_xingtangshi.png", False):
            log_message = log_creater.write_log(f"成功找到s-星糖石！位置在 {level_name} {level}-{number}")
            print(log_message)
            s_xingtangshi_list.append((level_name, level, number))
            break
###################################################################################################################################################
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
###################################################################################################################################################

def result_saver():
    result_folder = 'result'
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    result_file_path = os.path.join(result_folder, 'result.txt')
    
    content = ""
    content += "c-探索券：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in c_tansuoquan_list]) + "\n"
    content += "c-扫荡券：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in c_saodangquan_list]) + "\n"
    content += "c-体力药：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in c_tiliyao_list]) + "\n"
    content += "b-家具币：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in b_jiajvbi_list]) + "\n"
    content += "b-sr券：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in b_srquan_list]) + "\n"
    content += "b-金币：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in b_jinbi_list]) + "\n"
    content += "a-专武：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in a_zhuanwu_list]) + "\n"
    content += "a-ssr券：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in a_ssrquan_list]) + "\n"
    content += "s-星糖石：" + ",".join([f"{level_name}{level}-{number}" for level_name, level, number in s_xingtangshi_list]) + "\n"
    with open(result_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    with open(result_file_path, 'r', encoding='utf-8') as file:
        preview_content = file.read()
    print(f"结果已保存！预览：{preview_content}")

def sort_results():
    result_folder = 'result'
    result_file_path = os.path.join(result_folder, 'result.txt')
    processed_file_path = os.path.join(result_folder, 'processed_result.txt')

    with open(result_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = {
        "c-探索券": {"N": [], "H": [], "VH": []},
        "c-扫荡券": {"N": [], "H": [], "VH": []},
        "c-体力药": {"N": [], "H": [], "VH": []},
        "b-家具币": {"N": [], "H": [], "VH": []},
        "b-sr券": {"N": [], "H": [], "VH": []},
        "b-金币": {"N": [], "H": [], "VH": []},
        "a-专武": {"N": [], "H": [], "VH": []},
        "a-ssr券": {"N": [], "H": [], "VH": []},
        "s-星糖石": {"N": [], "H": [], "VH": []}
    }

    for line in lines:
        if line.strip():
            category, details = line.strip().split("：")
            items = details.split(",")
            for item in items:
                if item:
                    level_name, level_number = re.match(r'([^\d]+)(\d+-\d+)', item).groups()
                    data[category][level_name].append(f"{level_name}{level_number}")

    processed_content = ""
    for category, levels in data.items():
        processed_content += f"{category}：\n"
        for level_name, numbers in levels.items():
            if numbers:
                processed_content += f"  {level_name}：{','.join(numbers)}\n"
        processed_content += "\n"

    with open(processed_file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)

    print(f"分类已经完成！预览：\n{processed_content}")
###################################################################################################################################################
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
###################################################################################################################################################

def mining():

    log_message = log_creater.write_log("开始挖矿")
    print(log_message)
    while not image.co("task2.png"):
        image.co("task1.png")
    while not image.co("story.png",False):
        image.co("activity1.png")
        image.co("activity2.png")
    while not image.co("mininghome.png"):
        image.click(920,130,1)
    while not image.co("miningselect.png",False):
        image.co("go.png")

##########
##########     挖矿初始化
##########

    global n,h,n_,h_,vh,vh_
    complete_1_5 = False
    complete_5_10 = False
    complete_1_3 = False
    complete_1_1 = False
    image_ = image_list[n - 1]
    image__ = image_list[h - 1]
    image___ = image_list[vh - 1]

##########
##########     正在挖n级的矿
##########

    while not image.co("mininghome2.png",False) or image.co("h_.png",False):
        if n <=15:
            image.co(image_)
        else:
            break

    if n <= 15:  # and complete_1_5 == True:
        while n_ <= 5:
            for i in range(5):
                log_message = log_creater.write_log(f"正在挖N{n}-{n_}的矿")
                print(log_message)
                image.click(755 + i * 90, 530, 1)
                while not (image.co("success.png") or image.co("failure.png")):
                    log_message = log_creater.write_log(f"N{n}-{n_}的矿挖完了，开始识别")
                    print(log_message)
                sorting(n, n_, "N")
                n_ += 1
                while not image.co("mininghome3.png"):
                    image.co("ok2.png")
            complete_1_5 = True
            break

        while 6 <= n_ <= 10:
            if complete_1_5:
                complete_1_5 = False
                break
            for j in range(5):
                log_message = log_creater.write_log(f"正在挖N{n}-{n_}的矿")
                print(log_message)
                image.click(755 + j * 90, 630, 1)
                while not (image.co("success.png") or image.co("failure.png")):
                    log_message = log_creater.write_log(f"N{n}-{n_}的矿挖完了，开始识别")
                    print(log_message)
                sorting(n, n_, "N")
                n_ += 1
                while not image.co("mininghome3.png"):
                    image.co("ok2.png")
            complete_5_10 = True
            n += 1
            n_ = 1
            break

        # while n_ >=11:
        #     if complete_5_10:
        #         complete_5_10 = False
        #         break
        #     n += 1
        #     if n >= 16:
        #         break
        #     n_ = 1
        #     for i in range(5):
        #         print(f"正在挖{n}级第{n_}关的矿")
        #         image.click(755 + i * 90,530,1)
        #         while not (image.co("success.png") or image.co("failure.png")):
        #             print("ok")
        #         sorting(n,n_)
        #         n_ +=1
        #         while not image.co("mininghome3.png"):
        #             image.co("ok2.png")
        #     break
        
    while not image.co("task2.png",False):
        image.co("close.png")

##########
##########     挖完n级的矿了
##########

    while True:
        if image.co("h_.png"):
            break
        if image.co("h__.png"):
            log_message = log_creater.write_log("h准备开挖")
            print(log_message)
                

##########
##########     正在挖h级的矿
##########
    while not image.co("mininghome2.png",False):
        if h <= 15:
            image.co(image__)
        
    if h <=15:
        while h_ <= 3:
            for i in range(3):
                print(f"正在挖H{h}-{h_}的矿")
                image.click(755 + i * 90,530,1)
                while not (image.co("success.png") or image.co("failure.png")):
                    print(f"H{h}-{h_}的矿挖完了，开始识别")
                sorting(h,h_,"H")
                h_ +=1
                while not image.co("mininghome3.png"):
                    image.co("ok2.png")
            complete_1_3 = True
            break

        while 4 <= h_ <=6:
            if complete_1_3:
                complete_1_3 = False
                break
            for i in range(2):
                print(f"正在挖H{h}-{h_}的矿")
                image.click(755 + 3 * 90 + i * 90,530,1)
                while not (image.co("success.png") or image.co("failure.png")):
                    print(f"H{h}-{h_}的矿挖完了，开始识别")
                sorting(h,h_,"H")
                h_ +=1
                while not image.co("mininghome3.png"):
                    image.co("ok2.png")
            print(f"正在挖H{h}-{h_}的矿")
            image.click(755,630,1)
            while not (image.co("success.png") or image.co("failure.png")):
                print(f"H{h}-{h_}的矿挖完了，开始识别")
            sorting(h,h_,"H")
            h_ +=1
            while not image.co("mininghome3.png"):
                image.co("ok2.png")
            complete_1_3 = True
            break

        while 7 <= h_ <=9:
            if complete_1_3:
                complete_1_3 = False
                break
            for i in range(3):
                print(f"正在挖H{h}-{h_}的矿")
                image.click(755 + 90 + i * 90,630,1)
                while not (image.co("success.png") or image.co("failure.png")):
                    print(f"H{h}-{h_}的矿挖完了，开始识别")
                sorting(h,h_,"H")
                h_ +=1
                while not image.co("mininghome3.png"):
                    image.co("ok2.png")
            complete_1_3 = True
            break

        while h_ == 10:
            if complete_1_3:
                complete_1_3 = False
                break
            print(f"正在挖H{h}-{h_}的矿")
            image.click(755 + 4 * 90,630,1)
            while not (image.co("success.png") or image.co("failure.png")):
                print(f"H{h}-{h_}的矿挖完了，开始识别")
            sorting(h,h_,"H")
            h_ =1
            while not image.co("mininghome3.png"):
                image.co("ok2.png")
            h +=1
            complete_1_3 = True
            break
        
    while not image.co("task2.png",False):
        image.co("close.png")
##########
##########     正在挖vh级的矿
##########
    while True:
        if image.co("vh.png"):
            break
        if image.co("vh__.png"):
            break
        if image.co("vh_.png"):
            print("开始挖vh的矿")
                

##########
##########     正在挖vh级的矿
##########
    while not image.co("mininghome2.png",False):
        image.co(image___)
    if vh_ <=10:
        while vh_ <= 5:
            print(f'正在挖VH{vh}-{vh_}的矿')
            image.click(755 + (vh_ - 1) * 90,530,1)
            while not (image.co("success.png") or image.co("failure.png")):
                print(f"VH{vh}-{vh_}的矿挖完了，开始识别")

            sorting(vh,vh_,"VH")
            vh_ +=1
            while not image.co("mininghome3.png"):
                image.co("ok2.png")
            complete_1_1 = True
            break

        while 6 <= vh_ <=10:
            if complete_1_1:
                complete_1_1 = False
                break

            print(f'正在挖{vh}级第{vh_}关的矿')
            image.click(755 + (vh_ - 6) * 90,630,1)
            while not (image.co("success.png") or image.co("failure.png")):
                print(f"VH{vh}-{vh_}的矿挖完了，开始识别")

            sorting(vh,vh_,"VH")
            vh_ +=1
            while not image.co("mininghome3.png"):
                image.co("ok2.png")
            complete_1_1 = False
            #vh_ = 1
            break

    while not image.co("task2.png",False):
        image.co("close.png")


###################################################################################################################################################
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
###################################################################################################################################################

def main():
    chushi.delet()
    chushi.start_to_home()
    mining()
    result_saver()


while True:
    address_ = input("要挖的vh 写数字或者地图名称: ")
    found = False
    for pattern, value in address.items():
        if re.fullmatch(pattern, address_):
            vh = value
            print(f"将要挖这个地图: {vh}")
            found = True
            break
    if not found:
        print("没有这个图捏")
    break

while True:
    main()
    print(f"\n现在的运行情况:\n准备进行n级第{n}-{n_}关的挖矿\n准备进行n级第{h}-{h_}关的挖矿\nn级地图还差{150-(n-1)*10-n_+1}没挖\nh级地图还差{150-(h-1)*10-h_+1}没挖\nvh级地图还差{10-vh_+1}没挖")
    if h == 16:
        print(f"\n全部挖完了，请前往result文件夹查看挖矿结果")