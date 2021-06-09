import cv2
import numpy as np

capture = cv2.VideoCapture()
capture.op


#이미지 화질(카메라 세팅값)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

#이미지 시간 33을 쓰면 1초에 33장을 찍는다.(33밀리 세컨드 동안)
while cv2.waitKey(33)<0:
    ret, frame = capture.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(hsv, (5,10,10),(27,255,255))
    # H, S, V = cv2.inRange(hsv,cv2.COLOR_BGR2HSV)
    h,w = img_mask.shape[:2]
    # #새로운 배경 만들기
    # img_src = np.zeros((h,w,1), dtype=np.uint8)


    cv2.rectangle(frame,(w-50,h-50),(w,h),(255,0,0),2,cv2.LINE_8)
    face = cv2.bitwise_and(hsv,hsv,mask=img_mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    face = cv2.morphologyEx(face, cv2.MORPH_OPEN, kernel, iterations=1)
    face1 = cv2.cvtColor(face,cv2.COLOR_HSV2BGR)

    




    cv2.imshow("Video", face1)
    cv2.imshow("Video1", img_mask)
    cv2.imshow("Video2", frame)
    

#캡쳐 사용 해제
capture.release()


cv2.destroyAllWindows()