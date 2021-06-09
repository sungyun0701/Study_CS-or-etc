import RPi.GPIO as gpio
import time

  

gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

  

trig = 23

echo = 24

  

print ("start")

 

gpio.setup(trig, gpio.OUT)

gpio.setup(echo, gpio.IN)

 

try :

    while True :

      gpio.output(trig, False)

      time.sleep(0.5)

 

      gpio.output(trig, True)

      time.sleep(0.00001)

      gpio.output(trig, False)

 

      while gpio.input(echo) == 0 :

        pulse_start = time.time()

 

      while gpio.input(echo) == 1 :

        pulse_end = time.time()

 

      pulse_duration = pulse_end - pulse_start
      
      distance = pulse_duration * 17000

      distance = round(distance, 2)

 
      if distance<1000:
          print ("Distance : ", distance, "cm")
          if distance<80:
              gpio.output(16,True)
              gpio.output(20,False)
              gpio.output(21,False)
          if 80<distance<150:
              gpio.output(16,False)
              gpio.output(20,True)
              gpio.output(21,False)
          if 150<distance<1000:
              gpio.output(16,False)
              gpio.output(20,False)
              gpio.output(21,True)

except :

    gpio.cleanup()



    while gpio.input(echo) == 0 :

        pulse_start = time.time()

 

    while gpio.input(echo) == 1 :

        pulse_end = time.time()

 

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17000

    distance = round(distance, 2)