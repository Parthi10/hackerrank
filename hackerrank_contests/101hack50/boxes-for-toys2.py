#!/bin/python3

import sys
from itertools import combinations_with_replacement
from fractions import Fraction

def get_vol(a):
    return a[0]*a[1]*a[2]

n = int(input().strip())
toy_types = []
for a0 in range(n):
    ai, bi, ci = input().strip().split(' ')
    ai, bi, ci = [int(ai), int(bi), int(ci)]
    toy_types.append(sorted([ai,bi,ci]))


mat = [[None for x in range(n)] for y in range(n)]
volume_sum = 0
for i in range(n):
    mat[i][i]=toy_types[i]
    volume_sum += get_vol(mat[i][i])
# print(mat)
for l in range(2, n+1):
    for i in range(n-l+1):
        j = i + l - 1
        v1 = mat[i+1][j]
        v2 = mat[i][j-1]
        # print(i,j)
        mat[i][j] = [max(v1[0],v2[0]),max(v1[1],v2[1]),max(v1[2],v2[2])]
        volume_sum += get_vol(mat[i][j])


# print(volume_sum)
num = (n*(n+1))//2
f = Fraction(volume_sum, num)
m = 10**9 + 7
q =  f.denominator
p = f.numerator
q_inv = pow(q, m-2, m)
print((p*q_inv )% m)
