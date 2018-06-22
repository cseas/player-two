# Created by Abhijeet Singh
import pyautogui
import time

while True:
	button_loc = None
	while button_loc is None:
		button_loc = pyautogui.locateOnScreen('coins.png', confidence=0.9)
	buttonx, buttony = pyautogui.center(button_loc)
	pyautogui.click(buttonx, buttony)
	#pyautogui.click(x=576, y=391)
	time.sleep(5)

	button_loc = None
	while button_loc is None:
		button_loc = pyautogui.locateOnScreen('close.png', confidence=0.9)
	buttonx, buttony = pyautogui.center(button_loc)
	pyautogui.click(buttonx, buttony)
	#pyautogui.click(x=1160, y=506)
	time.sleep(3600)