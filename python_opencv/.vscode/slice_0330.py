import cv2

img_src = cv2.imread('images/pone.jpg', cv2.IMREAD_COLOR)

height, width = img_src.shape[:2]
print('height : ',height, 'width : ', width)

img_dst = cv2.pyrDown(img_src)
height, width = img_dst.shape[:2]
print('height : ',height, 'width : ', width)

img_dst1 = img_dst[150:620, 50:220].copy()
# img_dst2 = img_dst+50
img_tmp = cv2.cvtColor(img_dst1, cv2.COLOR_RGB2GRAY) # 3CH -> 1CH
img_tmp = cv2.cvtColor(img_tmp, cv2.COLOR_GRAY2BGR) # 1CH -> 3CH
img_dst[150:620, 50:220] = img_tmp

# cv2.imshow('Color1', img_src)
cv2.imshow('Color', img_dst)
cv2.imshow('dst1', img_dst1)
cv2.waitKey()
cv2.destroyAllWindows()