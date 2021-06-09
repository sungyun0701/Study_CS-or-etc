# CARServer.py
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import CarControl
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)


#CARControl.setup()

ctrCmd = ["8", "6", "4", "2", "5"]
#          앞,  오,  왼,  뒤,  스톱

while True:
        print('Waiting for connection')
        _, frame = capture.read()
        # 1CH로 변환
        frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # 이진화
        _, frame_binary = cv2.threshold(frame_gray, 100,120, cv2.THRESH_BINARY)

        # 클로징
        kernel = np.ones((7,7), np.uint8)
        frame_closing = cv2.morphologyEx(frame_binary,cv2.MORPH_CLOSE, kernel)

        # 윤곽선 찾기
        contours, hierarchy = cv2.findContours(frame_closing, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        for i, contour in enumerate(contours):
            if i>0 :
                CarControl.Forward()
            else:
                CarControl.Stop()
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
        
        

        

