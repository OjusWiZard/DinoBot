import pyautogui as gui
import time
from PIL import ImageGrab, ImageOps
from numpy import *

replayButton = (480,430)
dinoDanger = [170,457]
farSight = 150

def main():
	
	# Restart the Game
	gui.click(replayButton)
	gui.click(480,700)
	
	speedAdjust=0
	while True:
		
		#Get the pixels ahead
		dangerZone = (dinoDanger[0],dinoDanger[1],dinoDanger[0]+farSight,dinoDanger[1]+1)
		dangerImage = ImageGrab.grab(dangerZone)
		dangerGrayscaleImage = ImageOps.grayscale(dangerImage)
		danger = array(dangerGrayscaleImage.getcolors())
		sum = danger.sum()
		
		print(danger)
		
		speedAdjust+=1
		if(speedAdjust==3):
			dinoDanger[0]+=1
			speedAdjust=0
		if( danger[0][0]!=farSight ):
			gui.keyDown('up')
			print('JUMP')
		else:
			gui.keyUp('up')

main()