import os 
import pyautogui
import time 

#(20, 742) tool opener bar

#(575, 58) input text bar

pyautogui.FAILSAFE = True 

userInput = input("What do you want to search : ")

userInputssl = "https://{}".format(userInput)

userPrivateWindow = input("Do you want open private window (y/n) : ")

tool_open = True

def open_toolbar():
    pyautogui.click(20, 742)
    return

def type_text():
    pyautogui.click(575, 58)
    pyautogui.typewrite("goo")
    pyautogui.typewrite(["enter"])
    time.sleep(5)
    if (userPrivateWindow == "y") or (userPrivateWindow == "yes"):
        pyautogui.hotkey('ctrl', 'shift', 'n')

    return

def search_input():
    pyautogui.click(166, 80)
    pyautogui.typewrite(userInputssl)
    pyautogui.typewrite(["enter"])
    return

if userInput == '' or userPrivateWindow == '':
    print("Better Luck Next Time")
    exit()
else:
    open_toolbar()
    time.sleep(1)
    type_text()
    time.sleep(3)
    search_input()



