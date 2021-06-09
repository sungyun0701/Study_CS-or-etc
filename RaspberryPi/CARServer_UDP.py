# CARServer_UDP.py
import CARControl_UDP
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import sys


#CARControl.setup()

ctrCmd = ["FF", "RR", "BB", "LL", "FR", "BR", "FL", "BL", "SS", "PP"]
cmd = []

HOST = ''
PORT = 5900
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)

# 포트 설정
udpSerSock.bind(ADDR)
    
# 준비 완료 화면에 표시
print('udp echo server ready')

while True:
        print('Waiting for connection')
        data, addr = udpSerSock.recvfrom(BUFSIZE)
        print('...connected from :', addr)
        try:
                while True:
                    data = ''
                    data = udpSerSock.recv(BUFSIZE)
                    data = data.decode('utf-8')
                    print(data)
                    cmd = data.split(',')
                    if not data:
                        break
                    if cmd[0] == ctrCmd[0]:
                        CARControl_UDP.Forward(int(cmd[1]))
                        print("Forward")
                    if cmd[0] == ctrCmd[1]:
                        CARControl_UDP.Right(int(cmd[1]))
                        print("Right")
                    if cmd[0] == ctrCmd[2]:
                        CARControl_UDP.Backward(int(cmd[1]))
                        print("Backward")
                    if cmd[0] == ctrCmd[3]:
                        CARControl_UDP.Left(int(cmd[1]))
                        print("Left")
                    if cmd[0] == ctrCmd[4]:
                        CARControl_UDP.F_Right(int(cmd[1]))
                        print("Forward Right")
                    if cmd[0] == ctrCmd[5]:
                        CARControl_UDP.B_Right(int(cmd[1]))
                        print("Backward Right")
                    if cmd[0] == ctrCmd[6]:
                        CARControl_UDP.F_Left(int(cmd[1]))
                        print("Forward Left")
                    if cmd[0] == ctrCmd[7]:
                        CARControl_UDP.B_Left(int(cmd[1]))
                        print("Backward Left")
                    if cmd[0] == ctrCmd[8]:
                        CARControl_UDP.Stop()
                        print("Stop")
                    if cmd[0] == ctrCmd[9]:
                        print("Poweroff")
                        CARControl_UDP.Poweroff()
                        break
                        
                    
                        
        except KeyboardInterrupt:
            print("Terminated by Keborad Interrupt")
            GPIO.cleanup()
udpSerSock.close();


