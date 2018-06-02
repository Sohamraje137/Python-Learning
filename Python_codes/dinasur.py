import pyautogui
import time
import pyscreenshot as ImageGrab

class Coordinates():
	replaybtn=(300,340)
	dinasur=(171,395)

def restart():
	pyautogui.click(Coordinates.replaybtn)

def pressSpace():
	pyautogui.keyDown('space')
	time.sleep(0.05)
	print("jump")
	pyautogui.keyUp('space')

restart()
time.sleep(1)
pressSpace()