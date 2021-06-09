import cv2
#픽셀 중간에 튀는 부분이 있으면 거기서 오류검출이 될 경우가 있으므로
#blur를 사용하여 평균값으로 사용하여 튀는 부분을 없애서 노이즈를 없앨려고 사용
img_src = cv2.imread('images/fruit.jpg', cv2.IMREAD_COLOR)
img_src = cv2.pyrDown(img_src)
h, w = img_src.shape[:2]
print('h : ', h, 'w : ',w)

# dst = cv2.blur(src, ksize, anchor, borderType)는 입력 이미지(src)를 커널 크기(ksize), 고정점(anchor), 테두리 외삽법(borderType)
# 이미지가 작은데 블러(ksize)를 크게하면 이미지가 깨짐
# anchor=(-1,-1)로 하면 홀수로 이루어진 ksize의 중심을 나타냄
img_dst = cv2.blur(img_src, (9,9), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow('color',img_src)
cv2.imshow('dst',img_dst)
cv2.waitKey()
cv2.destroyAllWindows()