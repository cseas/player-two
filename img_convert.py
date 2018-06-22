# If pyautogui is not able to locate an image,
# convert it to RGB using this code.
# Created by Abhijeet Singh
import pyautogui

from PIL import Image

Image.open("close.png").convert("RGB").save("close.png")