import cv2

img_src = cv2.imread('images/tree.jpg',cv2.IMREAD_COLOR)
img_src = cv2.pyrDown(img_src)
h,w = img_src.shape[:2]
print('w : ',w, 'h : ',h)

# 이미지를 이진화 하기 위해서 3채널 영상을 1채널 영상으로 변환
# 컬러 이미지를 그레이 이미지로 변환
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

# 100보다 큰 값은 255가 되고 100보다 작으면 0으로 처리됨(255:흰색, 0:검정색)<--이런식으로 표현하는 것이 THRESH_BINARY
_, img_dst = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
_, img_dst_inv = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

# THRESH_TRUNC 100보다 작은 값은 그대로 사용하고 100보다 큰값은 100으로 사용
_, img_dst_trunc = cv2.threshold(img_gray, 100, 255, cv2.THRESH_TRUNC)

# THRESH_TOZERO 는 100보다 작은 값은 0으로 100보다 큰값은 그대로 사용
_, img_dst_TOZERO = cv2.threshold(img_gray, 100, 255, cv2.THRESH_TOZERO)
_, img_dst_TOZERO_inv = cv2.threshold(img_gray, 100, 255, cv2.THRESH_TOZERO_INV)

# 알고리즘을 통한 변환(인접한 값을 통해 여러가지 변환) // 적용형 알고리즘의 경우 임계값 필요 없음
_, img_dst_otsu = cv2.threshold(img_gray, 100, 255, cv2.THRESH_OTSU)
_, img_dst_triangle = cv2.threshold(img_gray, 100, 255, cv2.THRESH_TRIANGLE)

# 467들어간 부분은 홀수를 넣으면 된다. 하나의 픽셀을 계산할때 인접한 467개의 픽셀의 평균을 구한다.
# cv2.adaptiveThreshold(입력 이미지, 최댓값, 적응형 이진화 플래그, 임곗값 형식, 블록 크기, 감산값)을 의미합니다.
# 최대값이란 배경쪽에 나타낼 값, 블록크기는 인접한 픽셀중 어느 정도 픽셀을 참고 할것인지, 감산값은 평균을 해서 빼줄 값
img_dst_adap = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 467,37)

cv2.imshow('color',img_src)
cv2.imshow('gray',img_gray)
cv2.imshow('dst',img_dst)
cv2.imshow('dst_inv',img_dst_inv)
cv2.imshow('dst_trunc',img_dst_trunc)
cv2.imshow('dst_tozero',img_dst_TOZERO)
cv2.imshow('dst_tozero_inv',img_dst_TOZERO_inv)
cv2.imshow('dst_otsu',img_dst_otsu)
cv2.imshow('dst_triangle',img_dst_triangle)
cv2.imshow('dst_adap',img_dst_adap)
cv2.waitKey()
cv2.destroyAllWindows()