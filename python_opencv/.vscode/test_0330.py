import cv2

capture = cv2.VideoCapture('shin.mp4')
img_src1 = cv2.imread('images/ha.jpg',cv2.IMREAD_COLOR)

#카메라 세팅값
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

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
    gray = cv2.cvtColor(play_src, cv2.COLOR_BGR2GRAY)

    hi, wi= play_src.shape[:2]
    

    # slice를 통한 컬러이미지 흑백이미지 변환
    player_gray = play_src[hi//4:hi*3//4,wi//4:wi*3//4].copy()
    # 역상
    player_gray = cv2.bitwise_not(player_gray)
    # player_gray_tmp = cv2.cvtColor(player_gray,cv2.COLOR_BGR2GRAY) # 3CH -> 1CH
    # player_gray_tmp = cv2.cvtColor(player_gray_tmp,cv2.COLOR_GRAY2BGR) # 1CH -> 3CH
    play_src[hi//4:hi*3//4,wi//4:wi*3//4] = player_gray

    # 영상 1채널짜리 3채널로 바꾸기
    playcolor = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # flip을 통한 좌우 대칭
    gray1 = cv2.flip(gray, 10)
    
    # 영상(이미지)의 중심점은 (가로 : 이미지의 폭/2, 세로 : 이미지의 높이/2)
    matrix = cv2.getRotationMatrix2D((640/2, 480/2), 45, 1)
    # img_dst = cv2.warpAffine(원본 이미지, 회전 메트릭스, 적용할 영상의 크기(width, height))
    rotate = cv2.warpAffine(gray, matrix, (640, 480))
    rotate1 = cv2.warpAffine(ha_gray,matrix, (640, 480))
    # 이미지를 붙일려면 전부 흑백인지 컬러인지 확인도 하고 크기도 같아야 한다.
    merge = cv2.hconcat([gray,gray1,ha_gray])
    merge1 = cv2.vconcat([rotate, ha_gray])
    merge2 = cv2.vconcat([play_src, img_src1])
    merge3 = cv2.vconcat([rotate,rotate1])
    merge4 = cv2.vconcat([playcolor,img_src1])
    cv2.imshow('merge', merge)
    cv2.imshow('merge1', merge1)
    cv2.imshow('merge2', merge2)
    cv2.imshow('merge3', merge3)
    cv2.imshow('merge4', merge4)
    

#캡처 사용해제
capture.release()

cv2.destroyAllWindows()