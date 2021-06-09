# CARServer.py
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import CarControl


#CARControl.setup()

ctrCmd = ["8", "6", "4", "2", "5"]
#          앞,  오,  왼,  뒤,  스톱

while True:
        print('Waiting for connection')
        cmd = input()
        print('cmd :', cmd)
        if cmd == ctrCmd[0]:
            CarControl.Forward()
            print("Forward")
        if cmd == ctrCmd[1]:
            CarControl.Right()
            print("Right")
        if cmd == ctrCmd[2]:
            CarControl.Left()
            print("Left")
        if cmd == ctrCmd[3]:
            CarControl.Backward()
            print("Backward")
        if cmd == ctrCmd[4]:
            CarControl.Stop()
            print("Stop")
        
        

        
