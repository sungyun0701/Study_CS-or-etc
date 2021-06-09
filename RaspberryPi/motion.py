import RPi.GPIO as GPIO

import time



GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

pirPin = 18

GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)



while True:

    if GPIO.input(pirPin) == True:

        print ("Motion detected!")
        GPIO.output(23,True)
        time.sleep(1)
    else:

        print ("No motion")
        GPIO.output(23,False)
        time.sleep(1)
    