import pyautogui

with open("nothing.txt",'r')as f:
    for lines in f:
        pyautogui.write(lines)
        pyautogui.press("enter")