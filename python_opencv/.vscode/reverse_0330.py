import cv2

img_src = cv2.imread('images/crow.jpg',cv2.IMREAD_COLOR)
img_src = cv2.pyrDown(img_src)
h,w = img_src.shape[:2]

# 비트를 not연산을 한다. 0을 1로 1을 0으로
img_reverse = cv2.bitwise_not(img_src)
merge = cv2.hconcat([img_src,img_reverse])

cv2.imshow('src',img_src)
cv2.imshow('reverse',img_reverse)
cv2.imshow('merge',merge)
cv2.waitKey()
cv2.destroyAllWindows()
