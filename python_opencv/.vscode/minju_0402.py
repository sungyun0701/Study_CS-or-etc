import cv2

# 이미지 받아오기
capture = cv2.VideoCapture(0)

# 받아온 이미지 프레임 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# 노출 시간 / 33미리초만큼 기다린다 = 1초에 30번 받는다
while cv2.waitKey(33) < 0:
    ret, frame = capture.read()

    # BGR -> HSV 칼라공간 변화
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # H, S, V 로 색공간 분리
    H, S, V = cv2.split(frame_hsv)

    # H 로 살색 추출
    H_face = cv2.inRange(frame_hsv, (8,0,0), (20,255,250))
    frame_face = cv2.bitwise_and(frame_hsv, frame_hsv, mask=H_face)

    # 출력 위해 HSV -> BGR 변환
    frame_face = cv2.cvtColor(frame_face, cv2.COLOR_HSV2BGR)

    # 흑백 변환
    gray = cv2.cvtColor(frame_face, cv2.COLOR_BGR2GRAY)

    # 이진화
    
    # 오프닝 : e -> d
    opening_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    # o_e_result = cv2.erode(gray, opening_kernel, iterations=1)
    # o_d_result = cv2.dilate(o_e_result, opening_kernel, iterations=1)
    o_result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, opening_kernel)

    # 클로징 : d -> e
    closing_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    # c_d_result = cv2.dilate(o_d_result, closing_kernel, iterations=1)
    # c_e_result = cv2.erode(c_d_result, closing_kernel, iterations=1)
    c_result = cv2.morphologyEx(o_result, cv2.MORPH_CLOSE,closing_kernel)


    # 이진화
    _, binary = cv2.threshold(c_result, 80, 255, cv2.THRESH_BINARY)

    # 윤곽선 찾기
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for i, contour in enumerate(contours):
        if cv2.contourArea(contour) > 4000 :
            # x,y 좌측상단기준, 사각형 생성
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
 

    cv2.imshow("Video", frame)
    # cv2.imshow("Gray", gray)
    # cv2.imshow("Face", frame_face)
    # cv2.imshow("Opening", o_result)
    # cv2.imshow("Closing", c_result)
    # cv2.imshow("Binary", binary)

# 사용 후 해제
capture.release()

cv2.destroyAllWindows()