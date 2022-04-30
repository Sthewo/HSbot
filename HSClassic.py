#HSMerc.py
import pygetwindow as gw
import pyautogui
import time
from utilsHSMerc import matchTemplate

def checkScreen():
	
	if matchTemplate(screen,mana,0.7) != (0,0):
		x,y = 1000,350
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)

	elif matchTemplate(screen,confirmar) != (0,0):
		x,y = matchTemplate(screen,confirmar)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)

	elif matchTemplate(screen,chapa,0.6) != (0,0):
		x,y = matchTemplate(screen,chapa, 0.6)
		print(f'Las coordenadas son: ({x},{y})')
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
		x,y = (1280/2, 720/2)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
		time.sleep(15)


	elif matchTemplate(screen,jugar) != (0,0) and matchTemplate(screen,guerrero) != (0,0):
		x,y = matchTemplate(screen,guerrero)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
		x,y = matchTemplate(screen,jugar)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
		time.sleep(3)

	else:
		x,y = (1280/2, 710/2)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
		time.sleep(3)

chapa = 'Imagenes\\chapa.jpg'
confirmar = 'Imagenes\\confirmar.jpg'
jugar = 'Imagenes\\jugar.jpg'
click = 'Imagenes\\click.jpg'
mana = 'Imagenes\\1mana.jpg'
screen = 'screen.jpg'
derrota = 'Imagenes\\derrota1.jpg'
guerrero = 'Imagenes\\guerrero.jpg'

try:
	hs = gw.getWindowsWithTitle('Hearthstone')[0]
	print(hs)
	hs.resizeTo(1280, 720) # set size to 100x100
	hs.moveTo(0, 0) # move window to 10, 10
except:
	print('Hearthstone no esta abierto')

while True:
	screen_shot = pyautogui.screenshot()
	screen_shot.save('screen.jpg')
	checkScreen()
	print('loop')


