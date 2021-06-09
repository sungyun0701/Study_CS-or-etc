import cv2

capture = cv2.VideoCapture('shin.mp4')
img_src1 = cv2.imread('images/ha.jpg',cv2.IMREAD_COLOR)

# 동영상의 크기 알고 싶을 때 씀(while문 밖에서 써야함 그렇지 않으면 쓸데 없이 계속 호출되니까!!)
ret, frame = capture.read()
h, w= frame.shape[:2]
print(w, h)

height, width = img_src1.shape[:2]
print('height : ', height, 'width : ', width)

while cv2.waitKey(33)<0:
    # 비디오의 정보 중, 동영상의 현재 프레임 수(cv2.CAP_PROP_POS_FRAMES)와 동영상의 총 프레임 수(cv2.CAP_PROP_FRAME_COUNT)를 받아옵니다.
    # 비디오 속성 설정 메서드(capture.set)로 동영상의 현재 프레임을 초기화합니다.
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
         capture.open('shin.mp4')
    ret, frame = capture.read()
    play_src = cv2.resize(frame, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    img_src1 = cv2.resize(img_src1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    ha_gray = cv2.cvtColor(img_src1, cv2.COLOR_BGR2GRAY)
  
    hi, wi= play_src.shape[:2]
    
    # slice를 통한 컬러이미지 흑백이미지 변환
    player_gray = play_src[hi//4:hi*3//4,wi//4:wi*3//4].copy()
    player_gray_tmp = cv2.cvtColor(player_gray,cv2.COLOR_BGR2GRAY) # 3CH -> 1CH
    # _, player_gray_tmp = cv2.threshold(player_gray_tmp, 50, 255, cv2.THRESH_TRUNC)
    player_gray_tmp = cv2.adaptiveThreshold(player_gray_tmp, 205, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 167,17)
    player_gray_tmp = cv2.cvtColor(player_gray_tmp,cv2.COLOR_GRAY2BGR) # 1CH -> 3CH
    play_src[hi//4:hi*3//4,wi//4:wi*3//4] = player_gray_tmp

    merge = cv2.vconcat([play_src, img_src1])

    cv2.imshow('merge', merge)  

#캡처 사용해제
capture.release()

cv2.destroyAllWindows()