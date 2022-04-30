import pygetwindow as gw
import pyautogui

try:
	hs = gw.getWindowsWithTitle('Hearthstone')[0]
	print(hs)
	hs.resizeTo(640, 480) # set size to 100x100
	hs.moveTo(0, 0) # move window to 10, 10
except:
	print('Hearthstone no esta abierto')
	
screen_shot = pyautogui.screenshot()
screen_shot.save('screen.jpg')

pyautogui.moveTo(100,55)
pyautogui.click(100,55)	
