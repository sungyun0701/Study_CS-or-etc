import cv2
import numpy as np


img_src = cv2.imread("images/ni.jpg", cv2.IMREAD_COLOR)

# org = cv2.resize(org, dsize=(0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)  # ================  1 gray scale로 변환

kernel = np.ones((10, 5), np.uint8)
kernel2 = np.ones((6, 15), np.uint8)
roi_list = []

morph = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)  # 2 ================ 경계선 찾기

thr = cv2.adaptiveThreshold(morph, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 3, 30)  # 3 ================ 임계처리

morph2 = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel2)  # 4 ================ 뭉게기

contours, _ = cv2.findContours(morph2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 5 ================ 특징점 찾기

org2 = cv2.copyMakeBorder(img_src, 0, 0, 0, 0, cv2.BORDER_REPLICATE)
for cnt in contours:
    try:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 5 and 30 < h < 100:
            # print(w, h)
            roi = org2[y:y + h, x:x + w]
            # cv2.imshow('roi', roi)
            roi_list.append(roi)
            cv2.rectangle(img_src, (x, y), (x+w, y+h), (255, 0, 0), 2)

    except Exception as e:
        pass

cnt = 0              # print all pieces
'''for r in roi_list:
    cnt += 1
    cv2.imshow(str(cnt), r)'''

cv2.imshow('img_src', img_src)
# cv2.imshow('roi_list', roi_list)
cv2.imshow('gray', gray)
cv2.imshow('morph', morph)
cv2.imshow('morph2', morph2)
cv2.imshow('thr', thr)
cv2.waitKey()
cv2.destroyAllWindows()


