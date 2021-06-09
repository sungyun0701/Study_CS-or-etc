# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
#
# for i in range(5):
#     print(a[i]+b[i])
#
#
# import numpy as np
# e = np.array([1, 2, 3, 4, 5])
# f = np.array([6, 7, 8, 9, 10])
#
# print(e+f)

import numpy as np
import time

NUMBER_OF_CALC = 1000000 #파이썬에서 상수는 주로 대문자로 표기


#list 연산
start = time.time()
int_list_A = list(range(NUMBER_OF_CALC))
int_list_B = list(range(NUMBER_OF_CALC))

result = [x+y for x,y in zip(int_list_A, int_list_B)]
elapsed_time = time.time() - start
print(elapsed_time)

# numpy 배열 연산 numpy는 c언어로 구성 되어 있어서 빠르다.
start = time.time()
int_list_A = np.arange(NUMBER_OF_CALC)
int_list_B = np.arange(NUMBER_OF_CALC)
result = int_list_A + int_list_B
elapsed_time = time.time() - start
print(elapsed_time)
