# 5x - y = 9
# 2x + 3y = 7
# pip install scipy 하기
# numpy scipy sympy <== 이 3개가 solve를 지원하는 모듈임
import numpy as np
from scipy import linalg

# 행렬 정의
a = np.array([[5, -1], [2, 3]])

# 벡터 정의
b = np.array([8, 7])

# 해 구하기
x = linalg.solve(a, b)
print(x)

a = np.array([[4, 3], [3, 2]])
b = np.array([23, 16])
x = np.linalg.solve(a, b)
print(x)
