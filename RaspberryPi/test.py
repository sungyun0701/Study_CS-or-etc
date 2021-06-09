import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

while(True):
    GPIO.output(17,True)
    GPIO.output(27, False)
    GPIO.output(22, False)
    time.sleep(0.2)
    GPIO.output(17, False)
    GPIO.output(27,True)
    GPIO.output(22, False)
    time.sleep(0.2)
    GPIO.output(17, False)
    GPIO.output(27, False)
    GPIO.output(22,True)
    time.sleep(0.2)
