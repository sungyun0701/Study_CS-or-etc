import cv2

img_src = cv2.imread('images/circle.jpg', cv2.IMREAD_COLOR)
# img_src = cv2.pyrDown(img_src)

heigth, width = img_src.shape[:2]

# 이미지 그레이로 변환
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

# 그레이 이미지에서 원 찾기
circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, #그레이 이미지, 검출 방법
                            1,  # 해상도 비율
                            100, # 최소거리 (하나의 원을 찾았으면 그 원과 최소 100픽셀 안에서는 더이상 찾지 않는다..)
                            param1=250, param2= 10, # 케니엣지 임계값, 중심 임계값(값이 작으면 더 많은 원을 찾음)
                            minRadius=80, maxRadius=120) # 찾을 원의 최소 및 최대 반지름

for i in circles[0]:
    cv2.circle(img_src, (int(i[0]),int(i[1])),int(i[2]), (255,255,255),5)

cv2.imshow('src',img_src)
cv2.waitKey()
cv2.destroyAllWindows()