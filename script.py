import pyautogui
from random import randint
import time

def dosmth():
    rnd = randint(1, 5)
    if rnd == 1:
        pyautogui.hotkey('w')
        print(rnd)
        time.sleep(5)
        dosmth()
    elif rnd == 2:
        pyautogui.hotkey('a')
        time.sleep(5)
        print(rnd)
        dosmth()
    elif rnd == 3:
        pyautogui.hotkey('s')
        time.sleep(5)
        print(rnd)
        dosmth()
    elif rnd == 4:
        pyautogui.hotkey('d')
        time.sleep(5)
        print(rnd)
        dosmth()
    elif rnd == 5:
        pyautogui.click()
        time.sleep(5)
        print(rnd)
        dosmth()
dosmth()
