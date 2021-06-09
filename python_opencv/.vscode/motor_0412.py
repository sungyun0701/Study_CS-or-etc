import cv2
import numpy as np

capture = cv2.VideoCapture(0)

# 이미지 화질(카메라 세팅값)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# 캡처하기
while cv2.waitKey(33)<0:
    _, frame = capture.read()
    # 1CH로 변환
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 이진화
    _, frame_binary = cv2.threshold(frame_gray, 100,120, cv2.THRESH_BINARY)

    # 클로징
    kernel = np.ones((7,7), np.uint8)
    frame_closing = cv2.morphologyEx(frame_binary,cv2.MORPH_CLOSE, kernel)

    # 윤곽선 찾기
    contours, hierarchy = cv2.findContours(frame_closing, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for i, contour in enumerate(contours):
        if i>0 :
            CarControl.Forward()
        else:
            CarControl.Stop()

    cv2.imshow("Video1", frame)
    cv2.imshow("Video2", frame_binary)


capture.release()


cv2.destroyAllWindows()