import cv2
import numpy as np

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8): 
    try: 
        n = np.fromfile(filename, dtype) 
        img = cv2.imdecode(n, flags) 
        return img 
    except Exception as e: 
        print(e) 
        return None

# img_src = imread('images/4번 L50.bmp') 
# height, width = img_src.shape[:2]

# opencv는 기본적으로 한글 지원이 안되기 때문에 이미지를 불러올대 한글 있으면 안됨
# 위에 같이 쓰면 쓸수 있음
img_src = imread('test_img/10.bmp')

# 3CH -> 1CH gray로 변환
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

# 이진화(otsu threshole 적용)
_, img_binary = cv2.threshold(img_gray, 120,125, cv2.THRESH_OTSU)

# 모폴로지 연산 적용(클로징)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel = np.ones((5,5), np.uint8) #커널의 크기가 커지면 패인부분, 긁힘, 홀이 제거됨
img_binary = cv2.morphologyEx(img_binary, cv2.MORPH_CLOSE, kernel)  


# 윤곽선 찾기
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

count=0
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    M = cv2.moments(contour)
    cX = int(M['m10']/(M['m00']+1e-5))  #분모가 0이 되면 에러가 뜨기 때문에 (moment['m00']+1e-5)씀
    cY = int(M['m01']/(M['m00']+1e-5))
    # 원그리기 : cv2.circle(소스이미지, 중심점(pt), 반지름, (b,g,r), cv2.FILLED or -1)  <-- 채울때
    cv2.circle(img_src,(cX,cY),3,(255,0,0),-1)
    if cv2.contourArea(contour) > 5000 and 400<cX <2200 and 800<cY<1200 :
        if area >13000:
            cv2.drawContours(img_src,[contour], 0,(0,255,0),1)
            cv2.putText(img_src, '{}: {:.0f}'.format(i,area),(cX-60,cY+100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        else :
            cv2.drawContours(img_src,[contour], 0,(0,0,255),1)
            cv2.putText(img_src, '{}: {:.0f}'.format(i,area),(cX-60,cY+100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),1)
            count+=1

    if area> 5000 and 0<cX <300 and 600<cY<1100 :
        if area >10000:
            cv2.drawContours(img_src,[contour], 0,(0,255,0),1)
            cv2.putText(img_src, '{}: {:.0f}'.format(i,area),(cX+120,cY+20), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        else :
            cv2.drawContours(img_src,[contour], 0,(0,0,255),1)
            cv2.putText(img_src, '{}: {:.0f}'.format(i,area),(cX+120,cY+20), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),1)
            count+=1

    if area> 5000 and 2200<cX <2500 and 600<cY<1100 :
        if area >10000:
            cv2.drawContours(img_src,[contour], 0,(0,255,0),1)
            cv2.putText(img_src, '{}: {:.0f}'.format(i,area),(cX-250,cY+20), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        else :
            cv2.drawContours(img_src,[contour], 0,(0,0,255),1)
            cv2.putText(img_src, '{}: {:.0f}'.format(i,area),(cX-250,cY+20), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),1)
            count+=1
    
        # if hierarchy[0][i][3] == -1 :   
        #     cv2.putText(img_src, str(i),tuple(contour[0][0]), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        #     cv2.putText(img_src, str(cv2.contourArea(contour)),(tuple(contour[0][0])), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        # else : pass

        # # 면적 구하기
        # if hierarchy[0][i][3] == -1 :    
        #     number[count]=[float(count),cv2.contourArea(contour),0.0]
        # elif hierarchy[0][i][3] == i-1 :
        #     number[count-1][2]=cv2.contourArea(contour)
        # else :
        #     number[count]=[float(count),cv2.contourArea(contour),0.0]

        # print(i,':',number[i][0]-number[i][1])
  
        # cv2.imshow("src3", img_src)
        # cv2.waitKey()


if count == 0:
    cv2.putText(img_src, 'OK',(1230,300), cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)
else:
    cv2.putText(img_src, 'No',(1230,300), cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),3)


img_src = cv2.pyrDown(img_src)
img_gray = cv2.pyrDown(img_gray)
img_binary = cv2.pyrDown(img_binary)

cv2.imshow('src',img_src)
cv2.imshow('gray',img_gray)
cv2.imshow('binary',img_binary)

cv2.waitKey()
cv2.destroyAllWindows()