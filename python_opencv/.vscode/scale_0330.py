import cv2

img_src = cv2.imread('images/ha.jpg', cv2.IMREAD_COLOR)

height, width = img_src.shape[:2]
print('height : ', height, 'width : ', width)

#피라미드 개념으로 반으로 줄인다.
img_dst = cv2.pyrDown(img_src)
#또 반으로 줄이려면 pyrDown 한번 더 쓰면 됨
# 반대의 경우는 pyrUp임(최대 2배까지 할 수 있음)
height, width = img_dst.shape[:2]
img_up = cv2.pyrUp(img_dst, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT)

cv2.imshow('Color',img_src)
cv2.imshow('dst',img_dst)
cv2.imshow('up',img_up)
cv2.waitKey()
cv2.destroyAllWindows()