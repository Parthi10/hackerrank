#!/bin/python3

import sys

n = int(input().strip())
T = list(map(int, input().strip().split(' ')))
V = list(map(int, input().strip().split(' ')))

mat = [0]*n
mat[0] = V[0]
ans = V[0]
for i in range(1, n):
    new = mat[i-1] | V[i]
    if new != mat[i-1]:
        mat[i] = V[i]
        ans+= mat[i]
    else:
        mat[i] = new


# print(mat)
print(ans)
