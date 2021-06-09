import cv2
import numpy as np

img_src = cv2.imread('images/0408/1.bmp', cv2.IMREAD_COLOR)
img_dst = img_src.copy()
# 전처리를 진행하기 위해 그레이스케일 이미지(gray)와 케니 엣지 이미지(canny)를 사용합니다.
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
# 케니 엣지 알고리즘의 임곗값은 각각 5000과 1500로 주요한 가장자리만 남깁니다.
#커널은 5의 크기와 L2그라디언트를 True
_, img_binary = cv2.threshold(img_gray, 130, 180, cv2.THRESH_BINARY)
_, img_binary_inv = cv2.threshold(img_gray, 85, 110, cv2.THRESH_BINARY_INV)
canny = cv2.Canny(img_binary_inv, 5, 10, apertureSize = 7, L2gradient = True)
# 누산 평면은 각도 × 거리의 차원을 갖는 2차원 히스토그램으로 구성됩니다.
#cv2.HoughLines(검출 이미지, 
#               거리(0.0 ~ 1.0의 실수 범위), 각도(0 ~ 180), //누산 평면에서 사용되는 해상도를 나타냅니다.
#               임곗값, //허프 변환 알고리즘이 직선을 결정하기 위해 만족해야 하는 누산 평면의 값
#               거리 약수, 각도 약수, // 거리 약수와 각도 약수는 거리와 각도에 대한 약수(divisor)를 의미
#               최소 각도, 최대 각도)를 이용하여 직선 검출을 진행
# lines = cv2.HoughLines(canny, 0.8, np.pi /180, 150, srn=100,stn=200,min_theta=0,max_theta=np.pi)

# closing
kernel = np.ones((5,5), np.uint8)
img_closing = cv2.morphologyEx(img_binary, cv2.MORPH_CLOSE, kernel)
img_closing_inv = cv2.morphologyEx(img_binary_inv, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours(img_closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours_inv, hierarchy_inv = cv2.findContours(img_closing_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 150, minLineLength = 10, maxLineGap = 100)


for i in lines:
    cv2.line(img_dst, (i[0][0], i[0][1]), (i[0][2], i[0][3]), (0, 0, 255), 2)

# for i in lines:
#     rho, theta = i[0][0], i[0][1]
#     a, b = np.cos(theta), np.sin(theta)
#     x0, y0 = a*rho, b*rho

#     scale = img_src.shape[0] + img_src.shape[1]

#     x1 = int(x0 + scale * -b)
#     y1 = int(y0 + scale * a)
#     x2 = int(x0 - scale * -b)
#     y2 = int(y0 - scale * a)

#     cv2.line(img_dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
#     cv2.circle(img_dst, (x0, y0), 3, (255, 0, 0), 5, cv2.FILLED)

img_src = cv2.pyrDown(img_src)
img_dst = cv2.pyrDown(img_dst)
img_binary_inv = cv2.pyrDown(img_binary_inv)
img_gray = cv2.pyrDown(img_gray)
canny = cv2.pyrDown(canny)
cv2.imshow("dst", img_dst)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_binary_inv',img_binary_inv)
cv2.imshow('canny',canny)
cv2.waitKey()
cv2.destroyAllWindows()