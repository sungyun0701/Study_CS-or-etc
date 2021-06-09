import cv2

# 이미지 읽어옴
img_src = cv2.imread('images/glass.jpg', cv2.IMREAD_COLOR)

# 대칭 이미지 생성
img_flip = cv2.flip(img_src, 0)
img_flip_h = cv2.flip(img_src, 10)
# cv2.flip(src, flipCode)는 원본 이미지(src)에 대칭 축(flipCode)을 기준으로 대칭한 출력 이미지(dst)를 반환
# flipCode < 0은 XY 축 대칭(상하좌우 대칭)을 적용
# flipCode = 0은 X 축 대칭(상하 대칭)을 적용
# flipCode > 0은 Y 축 대칭(좌우 대칭)을 적용

# 이미지 붙이기
img_dst_v = cv2.vconcat([img_src,img_flip])
img_dst_v = cv2.pyrDown(img_dst_v)
# pyrDown 크기를 반으로 줄인다.


# 이미지 붙이기
img_dst_h = cv2.hconcat([img_src,img_flip_h])
img_dst_h = cv2.pyrDown(img_dst_h)

cv2.imshow('Color', img_src)
cv2.imshow("flip", img_flip)
cv2.imshow('merge', img_dst_v)
cv2.imshow('merge_h', img_dst_h)
cv2.imwrite('images/flip1.jpg',img_dst_v)
cv2.imwrite('images/flip2.jpg',img_dst_h)
cv2.waitKey()
cv2.destroyAllWindows()
# 모든 윈도우 창 제거 함수(cv2.destroyAllWindows)