import cv2 as cv
import numpy as np
import pyautogui
import pygetwindow as gw
import json

hs = gw.getWindowsWithTitle('Hearthstone')[0]
print(hs)
print(type(hs))
pyautogui.moveTo(980,580)
'''
for i in range(200,800,25):
	pyautogui.moveTo(i,370)
'''