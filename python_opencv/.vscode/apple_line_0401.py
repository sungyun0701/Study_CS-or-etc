import cv2

img_src = cv2.imread('images/apple.jpg', cv2.IMREAD_COLOR)
h,w = img_src.shape[:2]
print('h:',h,'w:',w)

cv2.rectangle(img_src, (30,50),(600,600),(250,0,0),3,cv2.LINE_8)

cv2.imshow('apple', img_src)
cv2.waitKey()
cv2.destroyAllWindows()