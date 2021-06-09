import cv2
import numpy as np

img_src = cv2.imread('images/contour.png', cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]

# 컬러 이미지를 그래이 이미지로 변환 (3CH -> 1CH)
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

# 그래이 이미지를 이진화 (추출해야할 부분을 threshold를 적용해서 흰색으로 추출)
_, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
# img_binary = cv2.bitwise_not(img_binary)

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# for i in range(len(contours)):
#     cv2.drawContours(img_src, [contours[i]],0,(0,255,0),2)
#     cv2.putText(img_src, str(i), tuple(contours[i][0][0]), \
#         cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0),1)
#     print(i, hierarchy[0][i])
#     cv2.imshow('src',img_src)
#     cv2.waitKey()


# for i in range(len(contours)):
#     cv2.drawContours(img_src,contours, i, (0,255,0), 2)
#     cv2.imshow('src', img_src)
#     cv2.waitKey()

count = 0 # contours[i] -> contour
for contour in contours:
    cv2.drawContours(img_src, [contour],0,(0,255,0),2)
    cv2.putText(img_src, str(count), tuple(contour[0][0]), \
        cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0),1)
    print(count, hierarchy[0][count])
    count+=1
    # cv2.imshow('src',img_src)
    # cv2.waitKey()

# cv2.drawContours(img_src,contours, -1, (0,255,0), 2)

num = 4
contours_min = np.argmin(contours[num], axis=0)
contours_max = np.argmax(contours[num], axis=0)

x_Min = contours[num][contours_min[0][0]][0][0]
y_Min = contours[num][contours_min[0][1]][0][1]
x_Max = contours[num][contours_max[0][0]][0][0]
y_Max = contours[num][contours_max[0][1]][0][1]

print("x-Min =", x_Min)
print("y-Min =", y_Min)
print("x-Max =", x_Max)
print("y-Max =", y_Max)

cv2.rectangle(img_src, (x_Min,y_Min),(x_Max,y_Max),(0,0,255), 1)
cv2.imshow('src', img_src)
cv2.imshow('gray', img_gray)
cv2.imshow('binary', img_binary)
cv2.waitKey()
cv2.destroyAllWindows()