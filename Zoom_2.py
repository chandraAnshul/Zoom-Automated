import pyautogui as auto
import time
from datetime import datetime
lst = [["user id",'password','startTime(hh:mm)','endTime(hh:mm)']]
isStarted = False

auto.press("win")
time.sleep(4)
auto.press('z')
time.sleep(4)
auto.press('enter')
time.sleep(4)
for i in range(7):
    auto.press('tab')
# auto.press('enter')

time.sleep(2)
for l in lst:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(l[2].split(':')[0]) and datetime.now().minute == int(l[2].split(':')[1]):
                auto.press('enter')
                auto.press('ab')
                time.sleep(2)
                for i in l[0]:
                    auto.press(i)
                auto.press('enter')
                time.sleep(6)
                auto.press('enter')
                auto.press('ab')
                time.sleep(2)
                for i in l[0]:
                    auto.press(i)
                time.sleep(3)
                auto.press('enter')
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(l[3].split(':')[0]) and datetime.now().minute == int(l[3].split(':')[1]):
                auto.press("enter")                         
                auto.keyDown('alt')
                auto.press('q')
                auto.keyUp('alt')
                isStarted = False
                break

time.sleep(5)
for i in range(5):
    auto.press('tab')

    
    
    
    
