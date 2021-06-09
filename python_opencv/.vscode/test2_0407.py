import cv2
import numpy as np

# def what(x):
#     origin = cv2.boundingRect(x)
#     return origin[0]

img_src = cv2.imread('images/11.bmp', cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]
# img_src1 = img_src.copy()
# 1CH로 변환
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

# 이진화
_, img_binary = cv2.threshold(img_gray, 120, 150, cv2.THRESH_OTSU)
_, img_binary_inv = cv2.threshold(img_gray,130, 180,cv2.THRESH_BINARY_INV)

# 클로징
kernel = np.ones((7,7), np.uint8)
img_closing = cv2.morphologyEx(img_binary,cv2.MORPH_CLOSE,kernel)
img_closing_inv = cv2.morphologyEx(img_binary_inv,cv2.MORPH_CLOSE,kernel)

# 윤곽선 찾기
contours, hierarchy = cv2.findContours(img_closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours_inv, hierarchy_inv = cv2.findContours(img_closing_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# contours.sort(key=lambda x: what(x))
count1=0
count2=0
x_di1 = []
x_di2 = []
for i, contour_inv in enumerate(contours_inv):
    area_inv = cv2.contourArea(contour_inv)
    if 50000<area_inv:
        # cv2.drawContours(img_src,[contour_inv], 0,(255,255,0),3)
        x,y,w,h = cv2.boundingRect(contour_inv)
        # cv2.rectangle(img_src,(x,y),(x+w,y+h),(0,0,255), 1)
        print(x,y,x+w,y+h)
        # cv2.line(img_src, (x-100, y+h-385), (x+w+100,y+h-385), (0,255,0), 2, cv2.LINE_AA)
        # cv2.line(img_src, (x-100, y+h-385-135), (x+w+100,y+h-385-135), (0,255,0), 2, cv2.LINE_AA)
        
print('밖에서',x,y,x+w,y+h)
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    # 모멘트 구하기
    M = cv2.moments(contour)
    cX = int(M['m10']/(M['m00']+1e-5))  #분모가 0이 되면 에러가 뜨기 때문에 (moment['m00']+1e-5)씀
    cY = int(M['m01']/(M['m00']+1e-5))
    
    if 1100<area<1650 and x < cX < x+w and y+h-385-135 < cY < y+h-385:
        cv2.drawContours(img_src,[contour], 0,(255,255,0),-1)
        cv2.circle(img_src,(cX,cY),5,(255,0,255),3)

        x_di1.append([cX,cY])
        # cv2.putText(img_src, '{}'.format(count1),(cX-10,cY+40), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,125,255),1)
        count1 +=1

    if 1300<area<1650 and x < cX < x+w and y+h-385 < cY < y+h-385+135:
        cv2.drawContours(img_src,[contour], 0,(255,0,255),-1)
        cv2.circle(img_src,(cX,cY),5,(255,255,255),3)
        
        x_di2.append([cX,cY])
        # cv2.putText(img_src, '{}'.format(count2),(cX-10,cY-40), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        count2 +=1

x_di1= sorted(x_di1)
x_di2= sorted(x_di2)
print(count1)
for i in range(count1):
    cv2.putText(img_src, '{}'.format(i+1),(x_di1[i][0]-10,x_di1[i][1]+40), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,125,255),1)

for i in range(count2):
    cv2.putText(img_src, '{}'.format(i+1),(x_di2[i][0]-10,x_di2[i][1]-30), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)

print(x_di1)
print(x_di2)

img_src = cv2.pyrDown(img_src)
img_closing_inv = cv2.pyrDown(img_closing_inv)
img_binary = cv2.pyrDown(img_binary)
img_closing = cv2.pyrDown(img_closing)
cv2.imshow('src',img_src)
# cv2.imshow('inv',img_closing_inv)
# cv2.imshow('binary',img_binary)
# cv2.imshow('closing',img_closing)

