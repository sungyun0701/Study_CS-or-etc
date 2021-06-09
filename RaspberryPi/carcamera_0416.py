import cv2
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import CarControl


capture = cv2.VideoCapture(-1)

#이미지 화질(카메라 세팅값)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
print('udp echo server ready')
#이미지 시간 33을 쓰면 1초에 33장을 찍는다.(33밀리 세컨드 동안)
while cv2.waitKey(33)<0:


    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(hsv, (8,0,0), (20,255,250))
    result = cv2.bitwise_and(frame,frame,mask=img_mask)
    h,w = img_mask.shape[:2]
    
    frame_face = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
    
    gray = cv2.cvtColor(frame_face, cv2.COLOR_BGR2GRAY)
    
    opening_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    o_result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, opening_kernel)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    camera = cv2.morphologyEx(o_result, cv2.MORPH_CLOSE, kernel, 1)
    
    _, binary = cv2.threshold(camera, 80, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i,contour in enumerate(contours):
        area = cv2.contourArea(contour)


        if 20000<area<60000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.drawContours(frame,[contour], -1,(0,0,255),2)
            CarControl.Forward()
            print(area)
            print("Forward")
            break
        elif area>100000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.drawContours(frame,[contour], -1,(0,0,255),2)
            CarControl.Backward()
            print(area)
            print("Backward")
            break
        else :
            CarControl.Stop()
            print(area)
            print("Stop")

    cv2.imshow("Video", frame)
#     cv2.imshow("Video1", camera)
#     cv2.imshow("Video2", result)
    
    

#캡쳐 사용 해제
capture.release()


cv2.destroyAllWindows()