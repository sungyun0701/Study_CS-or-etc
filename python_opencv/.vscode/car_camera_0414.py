import cv2
import imutils

capture = cv2.VideoCapture(0)

#이미지 화질(카메라 세팅값)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

#이미지 시간 33을 쓰면 1초에 33장을 찍는다.(33밀리 세컨드 동안)
while cv2.waitKey(33)<0:

    # (grabbed, frame) = capture.read()
 
    # # 프레임 크기를 조정, HSV 색으로 변환, lower upper 범위 HSV 픽셀 결정하기.
    # converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    # skinMask = cv2.inRange(converted,(0,40,80),(20,255,255)) 
 
  
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
   
 
    # skinMask = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # _,line,_ = cv2.findContours(skinMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
    # cv2.drawContours(frame, line, -1, (0,255,0), 3) 
    # cv2.imshow("images",frame) 

    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(hsv, (0,40,80),(30,255,255))
    h,w = img_mask.shape[:2]
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    camera = cv2.morphologyEx(img_mask, cv2.MORPH_CLOSE, kernel, 1)
    result = cv2.bitwise_and(frame,frame,mask=camera)

    contours, hierarchy = cv2.findContours(camera, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i,contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if 3000<area<10000:
            print("stop")
        if 10000<area<25000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.drawContours(frame,[contour], -1,(0,0,255),2)
            print("forward")
        if area>25000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.drawContours(frame,[contour], -1,(0,0,255),2)
            print("backward")
        

    cv2.imshow("Video", frame)
    cv2.imshow("Video1", camera)
    cv2.imshow("Video2", result)
    
    

#캡쳐 사용 해제
capture.release()


cv2.destroyAllWindows()