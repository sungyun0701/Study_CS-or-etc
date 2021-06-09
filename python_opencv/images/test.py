import cv2
import numpy as np

img_src = cv2.imread('images/apple.jpg',cv2.IMREAD_COLOR)
h, w = img_src.shape[:2]
img_b, img_g, img_r = cv2.split(img_src)
img_dst = cv2.merge((img_b,img_b,img_b))
zero = np.zeros((h,w,1),dtype=np.uint8)
img_dst1 = cv2.merge((img_b,zero,zero))

cv2.imshow('src',img_src)
# cv2.imshow('b',img_b)
# cv2.imshow('g',img_g)
# cv2.imshow('r',img_r)
cv2.imshow('dst',img_dst)
cv2.imshow('dst1',img_dst1)
cv2.waitKey()
cv2.destroyAllWindows()