import cv2
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


LEFT_PWM = 13 # ENABLE1 PIN
LEFT_FORWARD = 26 # INPUT1
LEFT_BACKWARD = 19 # INPUT2

RIGHT_PWM = 21 # ENABLE1 PIN
RIGHT_FORWARD = 20 # INPUT1
RIGHT_BACKWARD = 16 # INPUT2

GPIO.setup(LEFT_PWM, GPIO.OUT)
GPIO.setup(LEFT_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_BACKWARD, GPIO.OUT)

GPIO.setup(RIGHT_PWM, GPIO.OUT)
GPIO.setup(RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_BACKWARD, GPIO.OUT)

def forward():
    print ("forward motion")
    GPIO.output(LEFT_PWM, GPIO.HIGH)
    GPIO.output(LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(LEFT_BACKWARD, GPIO.LOW)

    GPIO.output(RIGHT_PWM, GPIO.HIGH)
    GPIO.output(RIGHT_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_BACKWARD, GPIO.LOW)


def backward():
    print ("backward motion")
    GPIO.output(LEFT_PWM, GPIO.HIGH)
    GPIO.output(LEFT_FORWARD, GPIO.LOW)
    GPIO.output(LEFT_BACKWARD, GPIO.HIGH)

    GPIO.output(RIGHT_PWM, GPIO.HIGH)
    GPIO.output(RIGHT_FORWARD, GPIO.LOW)
    GPIO.output(RIGHT_BACKWARD, GPIO.HIGH)


def stop():
    print ("stop")
    GPIO.output(LEFT_PWM, GPIO.LOW)
    GPIO.output(RIGHT_PWM, GPIO.LOW)
    

capture = cv2.VideoCapture(-1)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    # 원본(컬러)
    ret, frame = capture.read()
    cv2.imshow("Video", frame)
    
    # BGR -> HSV 칼라공간 변화
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # HSV 로 살색 추출
    HSV_face = cv2.inRange(frame_hsv, (8,0,0), (20,255,250))
    frame_face = cv2.bitwise_and(frame_hsv, frame_hsv, mask=HSV_face)
    
    # 출력 위해 HSV -> BGR 변환
    frame_face = cv2.cvtColor(frame_face, cv2.COLOR_HSV2BGR)
    
    # 흑백 변환
    gray = cv2.cvtColor(frame_face, cv2.COLOR_BGR2GRAY)
    
     # 오프닝 : e -> d
    opening_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    o_result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, opening_kernel)

    # 클로징 : d -> e
    closing_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    c_result = cv2.morphologyEx(o_result, cv2.MORPH_CLOSE,closing_kernel)


    # 이진화
    _, binary = cv2.threshold(c_result, 80, 255, cv2.THRESH_BINARY)
    
    # 윤곽선 찾기
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if 20000 < area < 60000 :
            # x,y 좌측상단기준, 사각형 생성
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            forward()
            print(area)
            break
        elif area > 100000 :
            # x,y 좌측상단기준, 사각형 생성
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            backward()
            print(area)
            break
        else :
            stop()
            print(area)
 

    cv2.imshow("Video", frame)
    
capture.release()
cv2.destroyAllWindows()