import cv2

# Hue(색상), Saturation(채도 : 선명도), Value(명도 : 밝기) h는 0~179, s와 v는 0~255
img_src = cv2.imread('images/tomato.jpg', cv2.IMREAD_COLOR)
height,width = img_src.shape[:2]
print('height : ', height, 'width : ', width)

# BGR 칼라공간 => HSV 칼라 공간으로 변환
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# HSV 색 공간을 각각 H, S, V로 분리
H, S, V = cv2.split(img_hsv)

# HSV의 H값으로 주황색 추출
# 그림판에서 색 스프로이드로 추출 후 그 값(RGU)을 https://www.rapidtables.com/convert/color/rgb-to-hsv.html 에서 계산해서 /2한 값
img_h = cv2.inRange(H,8,20)
img_r1 = cv2.inRange(H,0,5)
img_r2 = cv2.inRange(H,170,180)
img_lower_r = cv2.inRange(img_hsv,(0,0,0),(5,255,255))
img_upper_r = cv2.inRange(img_hsv,(170,0,0),(180,255,255))
added_r = cv2. addWeighted(img_lower_r,1.0,img_upper_r,1.0,0.0)
img_y = cv2.inRange(H,23,38)
img_g = cv2.inRange(H,60,75)
img_b = cv2.inRange(H,100,125)
img_p = cv2.inRange(H,140,165)

img_orange = cv2.bitwise_and(img_hsv,img_hsv,mask=img_h) # HSV
img_red1 = cv2.bitwise_and(img_hsv,img_hsv,mask=img_r1)
img_red2= cv2.bitwise_and(img_hsv,img_hsv,mask=img_r2)
img_yellow = cv2.bitwise_and(img_hsv,img_hsv,mask=img_y)
img_green = cv2.bitwise_and(img_hsv,img_hsv,mask=img_g)
img_blue =  cv2.bitwise_and(img_hsv,img_hsv,mask=img_b)
img_puple =  cv2.bitwise_and(img_hsv,img_hsv,mask=img_p)

img_add_red = cv2.bitwise_and(img_hsv,img_hsv,mask=added_r)
# 이미지를 출력하기 위해서 HSV->BGR로 변환
orange = cv2.cvtColor(img_orange, cv2.COLOR_HSV2BGR)
red1= cv2.cvtColor(img_red1, cv2.COLOR_HSV2BGR)
red2 = cv2.cvtColor(img_red2, cv2.COLOR_HSV2BGR)
yellow = cv2.cvtColor(img_yellow, cv2.COLOR_HSV2BGR)
green = cv2.cvtColor(img_green, cv2.COLOR_HSV2BGR)
blue =  cv2.cvtColor(img_blue, cv2.COLOR_HSV2BGR)
puple =  cv2.cvtColor(img_puple, cv2.COLOR_HSV2BGR)
add_red =  cv2.cvtColor(img_add_red, cv2.COLOR_HSV2BGR)



cv2.imshow('src', img_src)
cv2.imshow('hsv', img_hsv)
cv2.imshow('h', H)
cv2.imshow('s', S)
cv2.imshow('v', V)
cv2.imshow('img_orange', img_orange)
cv2.imshow('orange', orange)
cv2.imshow('red1', red1)
cv2.imshow('red2', red2)
cv2.imshow('yellow', yellow)
cv2.imshow('green', green)
cv2.imshow('blue', blue)
cv2.imshow('puple', puple)
cv2.imshow('add_red', add_red)
cv2.waitKey()
cv2.destroyAllWindows()