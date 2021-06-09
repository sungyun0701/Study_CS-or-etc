import cv2
import numpy as np

img_src = cv2.imread('images/contour.png', cv2.IMREAD_COLOR)

height, width = img_src.shape[:2]

print('height:',height,'width:',width)

# 칼라 이미지르 그레이 이미지로 변화(3CH -> 1CH)
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

# 그레이 이미지를 이진화(추출해야 할 부분을 threshold를 적용해서 흰색으로 추출)
_,img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
# img_binary = cv2.bitwise_not(img_binary) // INV를 안 쓰면 써준다.

# 윤곽선, 계층 구조를 반환한다 12개가됨
# cv2.findContours(이진화 이미지, 검색 방법, 근사화 방법)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

print('hierarchy:',hierarchy)
# hierarchy : [다음 윤곽선, 이전 윤곽선, 내곽 윤곽선, 외곽 윤곽선]

# for i in range(len(contours)):
#     cv2.drawContours(img_src,[contours[i]], 0,(0,0,255),2)
#     cv2.putText(img_src, str(i),tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
#     print(i, hierarchy[0][i])
#     cv2.imshow("src1", img_src)
#     cv2.waitKey()

# for i in range(len(contours)):
#     cv2.drawContours(img_src, contours, i, (0,255,0),2)
#     cv2.imshow("src2", img_src)
#     cv2.waitKey()

count = 0
for contour in contours:
    cv2.drawContours(img_src,[contour], 0,(0,0,255),2)
    cv2.putText(img_src, str(count),tuple(contour[0][0]), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
    print(count, hierarchy[0][count])
    count += 1
    cv2.imshow("src3", img_src)
    cv2.waitKey()

num = 4
contours_min = np.argmin(contours[num], axis=0)
contours_max = np.argmax(contours[num], axis=0)

x_Min = contours[num][contours_min[0][0]][0][0]
y_Min = contours[num][contours_min[0][1]][0][1]
x_Max = contours[num][contours_max[0][0]][0][0]
y_Max = contours[num][contours_max[0][1]][0][1]

cv2.drawContours(img_src, contours, -1, (0,255,0),2)
cv2.imshow('src',img_src)
cv2.imshow('gray',img_gray)
cv2.imshow('binary',img_binary)
cv2.waitKey()
cv2.destroyAllWindows()