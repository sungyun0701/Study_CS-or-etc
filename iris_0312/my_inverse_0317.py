# import numpy as np
#
# a = [[1, 0], [0,2]]
#
# b = np.linalg.inv(a)  #inv가 역행렬
# print(b)

a, b, c = map(int,input().split())
clist=[]
num = list(map(int,input().split()))
for i in num:
    clist.append(i)

clist.sort()
result = clist[0]*c*(b//c)+clist[1]*(b%c)