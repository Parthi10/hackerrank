#!/bin/python3

import sys
from collections import defaultdict


def two_pal(a,b, k_list):
    if a == b:
        return True
    for i in k_list:
        if a in i:
            if b in i:
                return True
            else:
                return False
        elif b in i:
            if a in i:
                return True
            else:
                return False
    return False

def longest_pal(a, m, k_list):
    mat = [[0 for x in range(m)] for y in range(m)]
    for x in range(m):
        mat[x][x] = 1

    for l in range(2, m+1):
        for i in range(m-l+1):
            j = i + l - 1
            if l==2 and two_pal(a[i], a[j], k_list):
                mat[i][j] = 2
            elif two_pal(a[i],a[j], k_list):
                mat[i][j] = 2 + mat[i+1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i+1][j])

    return mat[0][m-1]

def putInKList(x,y, k_list):
    for i in k_list:
        if (x in i) or (y in i):
            i.extend([x,y])
            return
    k_list.append([x,y])
k_list = []

n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    k_list.append([x,y])

k_dict = []
for i in sorted(k_list):
    putInKList(i[0],i[1], k_dict)

print(k_dict)

k_list = k_dict[:]
l = len(k_list)
for i in range(l):
    k_list[i] = set(k_list[i])


k_list = sorted(k_list, reverse=True)

a = list(map(int, input().strip().split(' ')))
print(k_list)
print(longest_pal(a, m, k_list))
