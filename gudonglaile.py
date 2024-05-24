
import os
import pyautogui
import time
import sys

def stopPyautoguiDetect(region):
    #当鼠标移动至窗口外时暂停循环
    mousePosition_x,mousePosition_y = pyautogui.position()
    if (mousePosition_x < region[0] or mousePosition_y < region[1] or
            mousePosition_x > region[0]+region[2] or mousePosition_y > region[1]+region[3]):
        sys.exit()
def locateImg(img:str, confidence:float, region:tuple=None):
    if not region:
        screenSize = pyautogui.size()
        region = (0, 0, screenSize[0], screenSize[1])
    position = pyautogui.locateOnScreen(img, confidence=confidence, region=region)
    return position
def clickMouse(x, y):
    pyautogui.click(x,y,duration=0.1)
def locateWindow(titlePath, confidence):
    #定位窗口
    while True:
        try:
            position = locateImg(titlePath, confidence=confidence)
            region = (position[0], position[1],
                    position[2], position[3]+735)
            break
        except:
            pass
    return region
def main(img, confidence, region):
    imgPath = "pic" + os.sep + img
    stopPyautoguiDetect(region)
    position = locateImg(imgPath, confidence, region)
    Center = pyautogui.center(position)
    clickMouse(Center[0], Center[1])

print("-----本程序开源且完全免费，请勿为程序付费，小红书号：26549571963，github:lxy554021379-----")
region = locateWindow(titlePath='pic/title.png', confidence=0.5)

while True:
    try:
        main("start.png",0.7, region)
    except:
        pass
    try:
        main("choise.png",0.5, region)
    except:
        pass
    i = 1
    while i <= 5:
        try:
            i += 1
            main("money.png",0.5, region)
            time.sleep(1)
            break
        except:
            pass
    try:
        main("ok.png",0.7, region)
    except:
        pass
    try:
        main("goon.png",0.7, region)
    except:
        pass
    try:
        main("close.png",0.8, region)
    except:
        pass
