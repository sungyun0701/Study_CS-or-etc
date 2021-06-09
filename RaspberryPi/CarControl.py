# CARControl.py
import RPi.GPIO as GPIO
import time
import sys


RIGHT_FORWARD = 20
RIGHT_BACKWARD = 16
RIGHT_PWM = 21
LEFT_FORWARD = 26
LEFT_BACKWARD = 19
LEFT_PWM = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(RIGHT_FORWARD,GPIO.OUT)
GPIO.setup(RIGHT_BACKWARD,GPIO.OUT)
GPIO.setup(RIGHT_PWM,GPIO.OUT)
GPIO.output(RIGHT_PWM,0)
RIGHT_MOTOR = GPIO.PWM(RIGHT_PWM,70)
RIGHT_MOTOR.start(0)
RIGHT_MOTOR.ChangeDutyCycle(0)

GPIO.setup(LEFT_FORWARD,GPIO.OUT)
GPIO.setup(LEFT_BACKWARD,GPIO.OUT)
GPIO.setup(LEFT_PWM,GPIO.OUT)
GPIO.output(LEFT_PWM,0)
LEFT_MOTOR = GPIO.PWM(LEFT_PWM,70)
LEFT_MOTOR.start(0)
LEFT_MOTOR.ChangeDutyCycle(0)

    
#RIGHT Motor control
def rightMotor(forward, backward, pwm):
    GPIO.output(RIGHT_FORWARD,forward)
    GPIO.output(RIGHT_BACKWARD,backward)
    RIGHT_MOTOR.ChangeDutyCycle(pwm)

#Left Motor control
def leftMotor(forward, backward, pwm):
    GPIO.output(LEFT_FORWARD,forward)
    GPIO.output(LEFT_BACKWARD,backward)
    LEFT_MOTOR.ChangeDutyCycle(pwm)
    
def Left():
    rightMotor(1 ,0, 60)            
    leftMotor(0 ,0, 0)
    
def Right():
    rightMotor(0 ,0, 0)            
    leftMotor(1 ,0, 60)
    
def Forward():
    rightMotor(1 ,0, 60)
    leftMotor(1 ,0, 60)
    
def Backward():
    rightMotor(0 ,1, 60)
    leftMotor(0 ,1, 60)

def Stop():
    rightMotor(0 ,0, 0)
    leftMotor(0 ,0, 0)
    
    
if __name__ == '__main__':
    pass
