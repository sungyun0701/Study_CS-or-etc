import cv2
import numpy as np

height = 720
width  = 1280
channel = 3

img_src = np.zeros((height,width,channel), dtype=np.uint8)

height , w = img_src.shape[:2]
# 선 그리기 : cv2.line(소스이미지, pt1, pt2, (color, b, g, r), 선굵기, 선형타입)
cv2.line(img_src, (100, 100), (width -100,100), (0,255,0), 2, cv2.LINE_AA)
# 좌표는 왼쪽 상단이 0,0이고 x는 오른쪽이 +, y는 아래쪽이 +

# 첫 왼쪽 상단 픽셀이 0,0 이므로 최외곽은 -1을 해줘야한다.
cv2.line(img_src, (0, 0), (width-1,height-1), (255,0,0), 2, cv2.LINE_AA)
cv2.line(img_src, (width-1, 0), (0,height-1), (255,0,0), 2, cv2.LINE_AA)

# 사각형 그리기 : cv2.rectangle(소스이미지, pt1, pt2, (color:b,g,r), 선굵기, cv2.field)
cv2.rectangle(img_src,(100,150),(300,400),(250,0,0), 3, cv2.LINE_8)
# 둘다 채우는 것
cv2.rectangle(img_src,(400,150),(600,400),(250,0,0), cv2.FILLED, cv2.LINE_8)
cv2.rectangle(img_src,(800,150),(1000,400),(250,50,0), -1)

# 원그리기 : cv2.circle(소스이미지, 중심점(pt), 반지름, (b,g,r), 선굵기, 선형타입)
# 원그리기 : cv2.circle(소스이미지, 중심점(pt), 반지름, (b,g,r), cv2.FILLED or -1)  <-- 채울때
cv2.circle(img_src, (500,550), 5, (0,255,0), -1)
cv2.circle(img_src, (500,550), 100, (0,0,255), 1, cv2.LINE_8)

# 타원 그리기
# img_dst = cv2.ellipse(img_src, center_pt, 소스이미지, 타원의 중심점,
#                       axes, angle, 메인축 방향의 반지름, 각도
#                       startAngle=, endAngle=, 호의 시작 각도, 호의 끝 각도
#                       color=, thickness=) 타원의 색, 태원의 두께(-1은 채우기가 됨)
#                       linetype는 안적 적어도 됨
center_pt = ((width//2),(height//2))
# 중심점에서 x축 방향으로 200, y축 방향으로 10인 노란색 타원 그리기(회전은 시계방향으로 회전한다.)
cv2.ellipse(img_src,center_pt, (200,10), 45,0,360,(0,255,255),2,cv2.LINE_AA)
# 중심점에서 x축 방향으로 10, y축 방향으로 20인 빨간색 타원 그리기
cv2.ellipse(img_src,center_pt, (10,200), 45,0,360,(0,0,255),2,cv2.LINE_AA)
# 중심점에서 x축 방향으로 200, y축 방향으로 200인 빨간색 타원 그리기
cv2.ellipse(img_src,center_pt, (200,200), 0,20,160,(255,0,0),2,cv2.LINE_AA)


# 폴리곤 그리기
pts1 = np.array([[100,500],[300,500],[200,600]])
pts2 = np.array([[600,500],[800,500],[700,600]])
# (img, pts, isClosed, color, thickness=..., lineType=..., shift=...) 
cv2.polylines(img_src, [pts1], True, (255,0,255), 2)
# (img, pts, color, lineType=..., shift=..., offset=...)
cv2.fillPoly(img_src, [pts2], (255,0,255), cv2.LINE_AA)

# 글자 쓰기(글자는 첫글자의 왼쪽 하단이 기준) // 한글이 안됨
# cv2.putText(img_src, "입력할 문자 : 한글 안됨", (기준점),  // 기준점은 글자의 좌측 하단 기준
#             글꼴, 글자크기,  // 4개의 글꼴이 있음 // 폰트에 따라 글자크기 달라짐
#             (글자색), 두께, 선형타이프)
# myString = "My name is %s"%('Sungyun') #python 2.x
myString = "My name is {}".format('Sungyun') #python 3.x
cv2.putText(img_src, myString, (400,400), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,0), 3)

cv2.imshow('src', img_src)
cv2.waitKey()
cv2.destroyAllWindows()