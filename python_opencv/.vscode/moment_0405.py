import cv2

img_src = cv2.imread('images/moment.png', cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]


img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
# 이진화
_, img_binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i, contour in enumerate(contours):
    M = cv2.moments(contour)
    cX = int(M['m10']/(M['m00']+1e-5))  #분모가 0이 되면 에러가 뜨기 때문에 (moment['m00']+1e-5)씀
    cY = int(M['m01']/(M['m00']+1e-5))
    print(cX)
    print(M['m10'])
    print(M['m00'])
    cv2.circle(img_src,(cX,cY),3,(255,0,0),-1)
    cv2.drawContours(img_src,[contour],0,(0,0,255),2)

cv2.imshow('src', img_src)
cv2.imshow('gray', img_gray)
cv2.imshow('binary', img_binary)


cv2.waitKey()
cv2.destroyAllWindows()