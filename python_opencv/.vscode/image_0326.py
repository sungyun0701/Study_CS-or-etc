# import cv2


# # 이미지 로드 (imread함수 사용)(imread('파일경로',파일타입))cv2.IMREAD_COLOR이나 cv2.IMREAD_ANYCOLOR아무거나 써도 됨
# img_src = cv2.imread('images/1.jpg', cv2.IMREAD_COLOR)

# cv2.imshow("Color",img_src)
# cv2.waitKey()
# cv2.destroyAllWindows()


import cv2

img = cv2.imread('images/1.jpg',cv2.IMREAD_COLOR)
if img is None:
    print('이미지 로딩 에러')
    exit(1)
cv2.imshow("Shin", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Shin1", img)

#이미지 저장하기 (파일경로및파일이름, 저장할 이미지)
cv2.imwrite('images/2.jpg',img)

cv2.waitKey()
cv2.destroyAllWindows()