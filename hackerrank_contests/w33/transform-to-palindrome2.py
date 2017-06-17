#!/bin/python3

import sys
from collections import defaultdict


def two_pal(a,b, k_list):
    if a == b:
        return True
    for i in k_list:
        if (a in i) and (b in i):
            return True
    return False

def longest_pal(a, m, k_list):
    mat = [[0 for x in range(m)] for y in range(m)]
    for x in range(m):
        mat[x][x] = 1

    for l in range(2, m+1):
        for i in range(m-l+1):
            j = i + l - 1
            if (l==2 and two_pal(a[i], a[j], k_list)):
                a[i] = a[j]
                mat[i][j] = 2
            elif two_pal(a[i],a[j], k_list):
                a[i] = a[j]
                mat[i][j] = 2 + mat[i+1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i+1][j])
    for i in mat:
        print(i)
    return mat[0][m-1]


k_dict = defaultdict(set)

n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    k_dict[x].add(y)
    k_dict[y].add(x)

a = list(map(int, input().strip().split(' ')))


def fill(i):
    values = k_dict[i]
    for value in values:
        k_dict.add(fill(value))



for i in k_dict:
    fill(i)

for i in k_dict:
    print(i, k_dict[i])


# print(k_list)
# print(longest_pal(a, m, k_list))
