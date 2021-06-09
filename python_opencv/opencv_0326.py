import cv2


#이미지 캡쳐(0으로하면 첫번째 카메라 1이면 두번째 카메라)
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture('video.webm')


#이미지 화질(카메라 세팅값)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

#이미지 시간 33을 쓰면 1초에 33장을 찍는다.(33밀리 세컨드 동안)
while cv2.waitKey(33)<0:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", frame)
    cv2.imshow("Gray", gray)

#캡쳐 사용 해제
capture.release()


cv2.destroyAllWindows()