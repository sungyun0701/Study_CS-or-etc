import cv2
import numpy as np

img_src = cv2.imread('images/sausages.jpg',cv2.IMREAD_COLOR)
img_src = cv2.pyrDown(img_src)
h,w = img_src.shape[:2]
print('h:',h,'w:',w)

# 빈 이미지 생성
# np.zeros((세로,가로,채널), 데이터 타입(8비트 0~255 : np.uint8)) unsigned int
zero = np.zeros((h, w, 1), dtype = np.uint8)

# 이미지(bgr)를 3개의 채널로 분리(b,g,r)
img_b, img_g, img_r = cv2.split(img_src)

# 분리된 이미지 채널을 3개 합쳐서 컬러로 만들 수 있다.
# img_merge = cv2.merge((img_b, img_g,img_r))

img_merge_b = cv2.merge((img_b,zero,zero))
img_merge_g = cv2.merge((zero,img_g,zero))
img_merge_r = cv2.merge((zero,zero,img_r))
img_merge_bg = cv2.merge((img_b,img_g,zero))


cv2.imshow('color',img_src)
cv2.imshow('b',img_b)
cv2.imshow('g',img_g)
cv2.imshow('r',img_r)
# cv2.imshow('merge',img_merge)
cv2.imshow('merge-b',img_merge_b)
cv2.imshow('merge-g',img_merge_g)
cv2.imshow('merge-r',img_merge_r)
cv2.imshow('merge-bg',img_merge_bg)

cv2.waitKey()
cv2.destroyAllWindows()