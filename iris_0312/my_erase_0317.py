# 4x - 3y = -9
# 3x - 7y = 17
# 행렬 계산 할 때  pip install numpy로 설치 하기

import numpy as np
my = np.array([[4, -3, -9], [3, -7, 17]])
print(len(my))
for i in range(len(my)):
    print(f'{my[i,0]}x {my[i,1]}y = {my[i,2]}')

# step1
# x의 계수를 곱하여 상하 교차 계수 정리
my_org = my.copy()
my[0] = my[0] * my_org[1,0]
my[1] = my[1] * my_org[0,0]

print('============step1=============')
for i in range(len(my)):
    print(f'{my[i, 0]}x {my[i, 1]}y = {my[i, 2]}')


# step2
# 위 식에서 아래 식을 뺀다
my[0] = my[0] - my[1]
print('============step2=============')
for i in range(len(my)):
    print(f'{my[i, 0]}x {my[i, 1]}y = {my[i, 2]}')


# step3
# 위 식에서 계수를 나누어 y해를 구한다.
my[0] = my[0] / my[0,1]
print('============step3=============')
for i in range(len(my)):
    print(f'{my[i, 0]}x {my[i, 1]}y = {my[i, 2]}')


# step4
# 아래 식에 y를 대입하고 우변으로 이동한다.
my[1,2] = my[1,2] - (my[1,1] * my[0,2])
my[1,1] = 0

print('============step4=============')
for i in range(len(my)):
    print(f'{my[i, 0]}x {my[i, 1]}y = {my[i, 2]}')

# step5
# 아래 식을 x의 계수로 나누어 x를 구한다.
my[1] = my[1] / my[1,0]
print('============step5=============')
for i in range(len(my)):
    print(f'{my[i, 0]}x {my[i, 1]}y = {my[i, 2]}')


# 참고용
ppl = True
num =12
my_test = f'{num:3d}' if ppl==False else f'+ {num}'
print(f'{my_test}')