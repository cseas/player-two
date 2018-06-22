# if pyautogui isn't able to locate image, run img_convert.py
import pyautogui
loc = None
while loc is None:
    loc = pyautogui.locateOnScreen('coins.png', confidence=0.9)
print(loc)