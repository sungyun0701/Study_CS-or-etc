import cv2

img_src = cv2.imread('images/crow.jpg', cv2.IMREAD_COLOR)
img_src = cv2.pyrDown(img_src)
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
h,w = img_gray.shape[:2]
print(h,w)
img_gray = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)

merge = cv2.hconcat([img_src,img_gray])
merge = cv2.resize(merge,dsize=(0,0),fx=0.7,fy=0.7)

cv2.imshow('src',img_src)
cv2.imshow('gray',img_gray)
cv2.imshow('merge',merge)
cv2.waitKey()
cv2.destroyAllWindows()