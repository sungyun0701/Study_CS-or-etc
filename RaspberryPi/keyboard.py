# CARServer.py
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import CarControl
import keyboard

#CARControl.setup()

ctrCmd = ["8", "6", "4", "2", "5"]
#          앞,  오,  왼,  뒤,  스톱

while True:
        print('Waiting for connection')
        
        
        if keyboard.on_pressed_key('w'):
            CarControl.Forward()
            print("Forward")
           
        if keyboard.on_pressed_key('d'):
            CarControl.Right()
            print("Right")
        
        if keyboard.on_pressed_key('a'):
            CarControl.Left()
            print("Left")
        
        if keyboard.on_pressed_key('s'):
            CarControl.Backward()
            print("Backward")
        else :
            CarControl.Stop()
            print("Stop")