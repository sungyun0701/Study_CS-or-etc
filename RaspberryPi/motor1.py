import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
pin1 = 20
pin2 = 21

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

try:
    while True:
        GPIO.output(pin1, True)
        GPIO.output(pin2, False)
        print('Motro1')
        time.sleep(2)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()