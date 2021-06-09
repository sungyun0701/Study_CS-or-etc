import RPi.GPIO as GPIO
import time

LED1 = 24
LED2 = 25
BUTTON = 18
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT, initial=False)
GPIO.setup(LED2, GPIO.OUT, initial=False)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LED1, False)
GPIO.output(LED2, False)
try:
        while True:
                key_in = GPIO.input(BUTTON)
                if key_in == 0:
                    if count ==0:
                        GPIO.output(LED1, True)
                        GPIO.output(LED2, False)
                        time.sleep(0.5)
                        count+=1
                    else:
                        GPIO.output(LED2, True)
                        GPIO.output(LED1, False)
                        time.sleep(0.5)
                        count = 0
                else:
                      pass
except KeyboardInterrupt:
    GPIO.cleanup()