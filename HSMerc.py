#HSMerc1.py
import pyautogui
import time
from utilsHSMerc import matchTemplate
def checkMenu():
	if matchTemplate(screen,elegir) != (0,0):
		x,y = matchTemplate(screen,elegir)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
def checkScreen():
	if matchTemplate(screen,elegir) != (0,0):
		x,y = matchTemplate(screen,elegir)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
	elif matchTemplate(screen,hoguera) != (0,0):
		x,y = matchTemplate(screen,jugar)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
	elif matchTemplate(screen,angel) != (0,0):
		x,y = matchTemplate(screen,angel)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
	elif matchTemplate(screen,relampagos) != (0,0):
		x,y = matchTemplate(screen,relampagos)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
	elif matchTemplate(screen,hasjugado) != (0,0):
		x,y = matchTemplate(screen,hasjugado)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
	elif matchTemplate(screen,aluchar) != (0,0):
		x,y = matchTemplate(screen,aluchar)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
	elif matchTemplate(screen,derrota) != (0,0):
		x,y = matchTemplate(screen,derrota)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
		time.sleep(2)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)
	else:
		x,y = (1280/2, 720/2)
		pyautogui.moveTo(x,y)
		pyautogui.click(x,y)

elegir = 'Imagenes\\elegir.jpg'
hoguera = 'Imagenes\\hoguera.jpg'
angel = 'Imagenes\\angel.jpg'
jugar = 'Imagenes\\jugar1.jpg'
click = 'Imagenes\\click.jpg'
derrota = 'Imagenes\\derrota.jpg'
hasjugado = 'Imagenes\\hasjugado.jpg'
relampagos = 'Imagenes\\relampagos.jpg'
aluchar = 'Imagenes\\aluchar.jpg'
screen = 'screen.jpg'

try:
	hs = gw.getWindowsWithTitle('Hearthstone')[0]
	print(hs)
	hs.resizeTo(1280, 720) # set size to 1280x720
	hs.moveTo(0, 0) # move window to 0, 0
except:
	print('Hearthstone no esta abierto')

screen_shot = pyautogui.screenshot()
screen_shot.save('screen.jpg')
checkScreen()
'''
while True:
	screen_shot = pyautogui.screenshot()
	screen_shot.save('screen.jpg')
	checkScreen()
	print('loop')
'''
