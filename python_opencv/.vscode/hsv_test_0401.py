import cv2
# Hue(색상), Saturation(채도 : 선명도), Value(명도 : 밝기) h는 0~179, s와 v는 0~255
img_src = cv2.imread('images/apple.jpg', cv2.IMREAD_COLOR)

height,width = img_src.shape[:2]
print('height : ', height, 'width : ', width)

# BGR 칼라공간 => HSV 칼라 공간으로 변환
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# 그림판에서 색 스프로이드로 추출 후 그 값(RGU)을 https://www.rapidtables.com/convert/color/rgb-to-hsv.html 에서 계산해서 /2한 값
img_lower_r = cv2.inRange(img_hsv,(0,35,10),(5,255,255))
img_upper_r = cv2.inRange(img_hsv,(170,35,10),(180,255,255))
added_r = cv2. addWeighted(img_lower_r,1.0,img_upper_r,1.0,0.0)

img_add_red = cv2.bitwise_and(img_hsv,img_hsv,mask=added_r)

# 이미지를 출력하기 위해서 HSV->BGR로 변환
add_red =  cv2.cvtColor(img_add_red, cv2.COLOR_HSV2BGR)
cv2.imshow('src', img_src)
cv2.imshow('hsv', img_hsv)
cv2.imshow('add_red', add_red)
cv2.waitKey()
cv2.destroyAllWindows()