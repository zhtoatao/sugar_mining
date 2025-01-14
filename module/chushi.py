from core import image, log_creater
import time
import pygame

'''
#def co(target_img,
        click_ = True,
        sleeptime=5,
        threshold=0.8,
        cv_method=cv2.TM_CCOEFF_NORMED)


def startapp():
    image.co("app.png")
    while not image.co("updating.png"):
        image.co("start.png")
        image.co("update.png")

        
def dayu():
    image.co("dayu.png")
    while not image.co("dayu_shutdwon.png"):
        image.co("skip.png")
        image.co("nowloading.png",False,4)

def datework():
    while not image.co("home1.png"):
        image.co("nowloading.png",False,5)
        while not image.co("home2.png"):
            image.co("nowloading.png",False,5)
            image.co("back.png")
            

while not image.co():
    image.co()            

'''

def delet():
    print("删除账号信息")
    while not image.co("setting.png"):
        image.co("menu.png",True,0.5)

    while not image.co("cancel.png",False):
        image.co("delet.png")
    
    while not image.co("ok.png"):
        image.co("delet.png")
    
    image.close_game_window("com.sugarconflict.sugarapp")

    print("删除完成")

def start_to_home():
    print("从桌面开始")
    while not image.co("bigok.png"):
        image.co("app.png")
    
    while not image.co("allskip.png"):
        image.co("tapstart.png")
        time.sleep(5)
    
    while not image.co("skip2.png"):
        image.co("skip.png")
    
def mining_():
    print("开始挖矿")
    while not image.co("task2.png"):
        image.co("task1.png")
    while not image.co("story.png",False):
        image.co("task1.png")
        image.co("task1.png")
    while not image.co("mininghome"):
        image.click(720,580,1)

