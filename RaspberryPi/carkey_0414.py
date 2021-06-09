# CARServer.py
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import CarControl
import pyautogui

#CARControl.setup()

ctrCmd = ["8", "6", "4", "2", "5"]
#          앞,  오,  왼,  뒤,  스톱

while True:
        print('Waiting for connection')
        
        if pyautogui.keyDown("w"):
            CarControl.Forward()
            print("Forward")
        
        if pyautogui.keyUp("d"):
            CarControl.Right()
            print("Right")
       
        if pyautogui.keyUp("a"):
            CarControl.Left()
            print("Left")
      
        if pyautogui.keyUp("d"):
            CarControl.Backward()
            print("Bakc")
#         elif pyautogui.keyUp(ctrCmd[3]):
#             CarControl.Stop()
#             print("Stop")