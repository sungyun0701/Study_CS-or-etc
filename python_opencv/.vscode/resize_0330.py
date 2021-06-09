import cv2

img_src = cv2.imread('images/glass.jpg',cv2.IMREAD_COLOR)

height, width = img_src.shape[:2]
print('height : ',height, 'width : ', width)
img_dst = cv2.resize(img_src, dsize=(640,480), interpolation=cv2.INTER_AREA)
img_dst1 = cv2.resize(img_src, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow('img_src',img_src)
cv2.imshow('img_dst',img_dst)
cv2.imshow('img_dst1',img_dst1)
cv2.waitKey()
cv2.destroyAllWindows()