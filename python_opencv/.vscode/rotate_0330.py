import cv2

img_src = cv2.imread('images/tu.jpg',cv2.IMREAD_COLOR)
img_src1 = cv2.imread('images/ha.jpg',cv2.IMREAD_COLOR)

height, width = img_src.shape[:2]
# shape[:2]째 까지 // 안쓰면 channel까지 써야한다.
#  그러나 쓰게 되면 흑백사진에서는 channel이 1이라서 생략되는 경우가 생겨 opencv에서 오류가 발생
print(height, width)
# 밑에 출력창에 height, width 크기가 나온다.

# 이미지를 컬러에서 흑백으로 변환
img_gray  = cv2.cvtColor(img_src1, cv2.COLOR_BGR2GRAY)
height, width = img_gray.shape[:2]
print(height, width)

# matrix = cv2.getRotationMatrix2D((회전 할 중심점), 회전할 각도, 스케일)
# 영상(이미지)의 중심점은 (가로 : 이미지의 폭/2, 세로 : 이미지의 높이/2)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
# img_dst = cv2.warpAffine(원본 이미지, 회전 메트릭스, 적용할 영상의 크기(width, height))
img_dst = cv2.warpAffine(img_src, matrix, (width, height))


cv2.imshow('Color',img_src)
cv2.imshow('dst', img_dst)
cv2. imshow('Gray',img_gray)
cv2.waitKey()
cv2.destroyAllWindows()