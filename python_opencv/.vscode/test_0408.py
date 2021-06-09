import cv2
import numpy as np

img_src = cv2.imread('images/0408/1.bmp',cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]

# 1CH
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

# 2진화
_, img_binary = cv2.threshold(img_gray, 130, 180, cv2.THRESH_BINARY)
_, img_binary_inv = cv2.threshold(img_gray, 90, 180, cv2.THRESH_BINARY_INV)

# closing
kernel = np.ones((5,5), np.uint8)
img_closing = cv2.morphologyEx(img_binary, cv2.MORPH_CLOSE, kernel)
img_closing_inv = cv2.morphologyEx(img_binary_inv, cv2.MORPH_CLOSE, kernel)

# 윤곽선 찾기
contours, hierarchy = cv2.findContours(img_closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours_inv, hierarchy_inv = cv2.findContours(img_closing_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

canny = cv2.Canny(contours_inv, 500, 1500, apertureSize = 5, L2gradient = True)
lines = cv2.HoughLines(canny, 0.8, np.pi /180, 150, srn=100,stn=200,min_theta=0,max_theta=np.pi)


x_di1 = []
x_di2 = []
c_count = 0
for i, contour_inv in enumerate(contours_inv):
    area_inv = cv2.contourArea(contour_inv)
    if 50000<area_inv:
        cv2.drawContours(img_src,[contour_inv], 0,(255,255,0),3)
        x,y,w,h = cv2.boundingRect(contour_inv)
        cv2.rectangle(img_src,(x,y),(x+w,y+h),(0,0,255), 1)
        # print(x,y,x+w,y+h)
        

for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    # 모멘트 구하기
    M = cv2.moments(contour)
    cX = int(M['m10']/(M['m00']+1e-5))  #분모가 0이 되면 에러가 뜨기 때문에 (moment['m00']+1e-5)씀
    cY = int(M['m01']/(M['m00']+1e-5))

    # 왼쪽
    if 500<area<1100 and x+200 < cX < x+304 and y < cY < y+1300:
        cv2.drawContours(img_src,[contour], 0,(255,255,0),-1)
        cv2.circle(img_src,(cX,cY),5,(255,0,255),3)
        x_di1.append([cX,cY])
        # cv2.putText(img_src, '{}'.format(count1),(cX-10,cY+40), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,125,255),1)
        
    # 오른쪽
    if 500<area<1100 and x+304 < cX < x+410 and y < cY < y+1300:
        cv2.drawContours(img_src,[contour], 0,(255,0,255),-1)
        cv2.circle(img_src,(cX,cY),5,(255,255,255),3)
        x_di2.append([cX,cY])
        # cv2.putText(img_src, '{}'.format(count2),(cX-10,cY-40), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)

    # 문자 인식
    if 1100<area<9000 and x+608 < cX < x+1100 and y < cY < y+1300:
        cv2.drawContours(img_src,[contour], 0,(255,0,255),-1)
        cv2.circle(img_src,(cX,cY),5,(255,255,255),3)
        x_c,y_c,w_c,h_c = cv2.boundingRect(contour)
        cv2.rectangle(img_src,(x_c,y_c),(x_c+w_c,y_c+h_c),(100,0,255), 1)
        c_count += 1


        
x_di1= sorted(x_di1, key=lambda x : x[1])
x_di2= sorted(x_di2, key=lambda x : x[1])
print(x_di1)
print(x_di2)
print(c_count)
for i in range(len(x_di1)):
    cv2.putText(img_src, '{}'.format(i+1),(x_di1[i][0]+30,x_di1[i][1]+10), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,125,255),1)

for i in range(len(x_di1),(len(x_di1)+len(x_di2))):
    cv2.putText(img_src, '{}'.format(i+1),(x_di2[i-len(x_di1)][0]-50,x_di2[i-len(x_di1)][1]), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)

img_src=cv2.pyrDown(img_src)
img_gray=cv2.pyrDown(img_gray)
img_binary=cv2.pyrDown(img_binary)
img_closing=cv2.pyrDown(img_closing)
img_closing_inv=cv2.pyrDown(img_closing_inv)
cv2.imshow('src',img_src)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_closing_inv',img_closing_inv)
cv2.imshow('img_binary',img_binary)
cv2.imshow('img_closing',img_closing)
cv2.waitKey()
cv2.destroyAllWindows()