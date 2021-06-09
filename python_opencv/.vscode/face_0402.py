import cv2
import numpy as np

capture = cv2.VideoCapture(0)


#이미지 화질(카메라 세팅값)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

#이미지 시간 33을 쓰면 1초에 33장을 찍는다.(33밀리 세컨드 동안)
while cv2.waitKey(33)<0:
    ret, frame = capture.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(hsv, (5,10,10),(27,255,250))
    # H, S, V = cv2.inRange(hsv,cv2.COLOR_BGR2HSV)
    h,w = img_mask.shape[:2]
    
    
    face_mask = cv2.bitwise_and(hsv,hsv,mask=img_mask)

    face1 = cv2.cvtColor(face_mask,cv2.COLOR_HSV2BGR)
    face1 = cv2.cvtColor(face1,cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(face1, 80, 255, cv2.THRESH_BINARY)

    # 오프닝???
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    face_mask = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

    # 클로징
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    face_mask = cv2.morphologyEx(face_mask, cv2.MORPH_CLOSE, kernel)    

    contours, hierarchy = cv2.findContours(face_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)


    for i, contour in enumerate(contours):
        if(cv2.contourArea(contour) > 3000):
            # cv2.drawContours(frame, [contour],0,(0,0,255),2)
            #픽셀단위
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255), 1)
        
 

    cv2.imshow("binary", binary)
    cv2.imshow("Video", face1)
    cv2.imshow("Video1", img_mask)
    cv2.imshow("Video2", frame)
    

#캡쳐 사용 해제
capture.release()


cv2.destroyAllWindows()