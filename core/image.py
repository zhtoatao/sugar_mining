import os
import subprocess
import cv2
import time
import random
from . import log_creater,parame_reader

current_folder = os.getcwd()
adb_path, adb_port = parame_reader.read_adb_address()
parame_reader.run_adb(adb_path, adb_port)
adb_command = [
    '"{}"'.format(adb_path),
    "-s",
    "127.0.0.1:{}".format(adb_port),
]
adb_command_str = " ".join(adb_command)



#简单的点击动作
def click(x, y, sleeptime,maxoffset=5):
    random_x = x + random.randint(0,maxoffset)
    random_y = y + random.randint(0,maxoffset)
    command = f"{adb_command_str} shell input tap {random_x} {random_y}"
    subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    log_message = log_creater.write_log(f"----------图片中心点击: "+str(x)+","+str(y))
    print(log_message)

    time.sleep(sleeptime)

#简单滑动操�?
def swipe(x1, y1, x2, y2, waittime):
    random_r1 = random.randint(-10,10)
    random_r2 = random.randint(-10,10)
    command = f"{adb_command_str} shell input swipe {x1 + random_r1} {y1 + random_r2} {x2+ random_r1} {y2 - random_r2}"
    subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    time.sleep(waittime)


#adb截屏指令
def screen_shot():
    screenshot_file = os.path.join(current_folder, "screenshot", "screenshot.png")
    subprocess.run(f"{adb_command_str} exec-out screencap -p > {screenshot_file}", shell=True, check=True)
    return screenshot_file


#check only once,没check到就false，check到了就true，可以选择点和不点
def co(target_img,click_ = True,sleeptime=0.2,threshold=0.8,cv_method=cv2.TM_CCOEFF_NORMED):
    target = os.path.join(current_folder, "target", target_img)
    screenshot = cv2.imread(screen_shot())
    target_image = cv2.imread(target)
    result = cv2.matchTemplate(screenshot, target_image, cv_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        log_message = log_creater.write_log(f"----------找到 {target_img} 力")
        print(log_message)
        if click_:
            center_x = max_loc[0] + target_image.shape[1] // 2
            center_y = max_loc[1] + target_image.shape[0] // 2
            click(center_x,center_y,sleeptime)
        return True
    else:
        log_message = log_creater.write_log(f"----------找不到 {target_img}")
        print(log_message)
        return False

#write text,输入字符
def wt(text, sleeptime=1):
    for char in text:
        command = f"{adb_command_str} shell input text {char}"
        subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        time.sleep(sleeptime)
    log_message = log_creater.write_log(f"----------输入文本: {text}")
    print(log_message)

#关闭游戏
def close_game_window(package_name):
    command = f"{adb_command_str} shell am force-stop {package_name}"
    subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    log_message = log_creater.write_log(f"----------关闭游戏窗口: {package_name}")
    print(log_message)
    time.sleep(1)