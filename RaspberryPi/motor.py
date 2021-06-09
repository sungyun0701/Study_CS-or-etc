from gpiozero import Motor
import time

motor = Motor(20, 21)

while True:
    print('모터 회전 방향 : Forward')
    motor.forward()
    time.sleep(5)
    
    print('모터 회전 방향 : Backward')
    motor.backward()
    time.sleep(5)
