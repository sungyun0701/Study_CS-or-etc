import cv2

img_src = cv2.imread('images/coins.png', cv2.IMREAD_COLOR)

h, w = img_src.shape[:2]
print('w : ',w, 'h : ',h)

# color -> gray
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
# CV_8U 언사인드 8bit
# 입력 이미지(src)에 출력 이미지 정밀도(ddepth)를 설정하고 dx(X 방향 미분 차수), dy(Y 방향 미분 차수), 커널 크기(ksize), 비율(scale), 오프셋(delta), 테두리 외삽법(borderType)
img_sobel  = cv2.Sobel(img_gray, cv2.CV_8U, 2, 2, 3)
# 입력 이미지(src)에 출력 이미지 정밀도(ddepth)를 설정하고 커널 크기(ksize), 비율(scale), 오프셋(delta), 테두리 외삽법(borderType)
img_laplacian = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = 3)
# 입력 이미지(src)를 하위 임곗값(threshold1), 상위 임곗값(threshold2), 소벨 연산자 마스크 크기(apertureSize), L2 그레이디언트(L2gradient)
img_canny = cv2.Canny(img_gray,100, 255)

cv2.imshow('color',img_src)
cv2.imshow('sobel',img_sobel)
cv2.imshow('laplacian',img_laplacian)
cv2.imshow('canny',img_canny)
cv2.waitKey()
cv2.destroyAllWindows()