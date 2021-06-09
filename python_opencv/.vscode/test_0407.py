import cv2
import numpy as np

def what(x):
    origin = cv2.boundingRect(x)
    return origin[0]

img_src = cv2.imread('images/1.bmp', cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]
img_src1 = img_src.copy()
# 1CH로 변환
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

# 이진화
_, img_binary = cv2.threshold(img_gray, 120, 150, cv2.THRESH_OTSU)

# 클로징
kernel = np.ones((7,7), np.uint8)
img_closing = cv2.morphologyEx(img_binary,cv2.MORPH_CLOSE,kernel)

# 윤곽선 찾기
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contours.sort(key=lambda x: what(x))

# contours=sorted(contours, key = lambda x: x[0])
count1=1
count2=1
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    
    # 모멘트 구하기
    M = cv2.moments(contour)
    cX = int(M['m10']/(M['m00']+1e-5))  #분모가 0이 되면 에러가 뜨기 때문에 (moment['m00']+1e-5)씀
    cY = int(M['m01']/(M['m00']+1e-5))
    
    if 1100<area<1650 and 500 < cX < 2050 and 850 < cY < 920:
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(img_src,(x,y),(x+w,y+h),(0,0,255), 2)

        cv2.drawContours(img_src,[contour], 0,(255,255,0),-1)
        cv2.circle(img_src,(cX,cY),5,(255,0,255),-1)
        cv2.putText(img_src, '{}'.format(count1),(x-10,y-40), cv2.FONT_HERSHEY_COMPLEX,0.8,(200,125,255),1)
        count1 +=1

    if 1300<area<1650 and 500 < cX < 2050 and 1000 < cY < 1121:
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(img_src,(x,y),(x+w,y+h),(0,255,0), 2)
        cv2.drawContours(img_src,[contour], 0,(255,0,255),-1)
        cv2.circle(img_src,(cX,cY),5,(255,255,255),-1)
        cv2.putText(img_src, '{}'.format(count2),(cX-10,cY-40), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        count2 +=1
 
img_src = cv2.pyrDown(img_src)
img_src1 = cv2.pyrDown(img_src1)
img_binary = cv2.pyrDown(img_binary)
img_closing = cv2.pyrDown(img_closing)
cv2.imshow('src',img_src)
cv2.imshow('src1',img_src1)
cv2.imshow('binary',img_binary)
cv2.imshow('closing',img_closing)
cv2.waitKey()
cv2.destroyAllWindows()
