#!/bin/python3

import sys
from itertools import combinations

def pythagoreanTriple(a):
    if a%2==0:
        b = (a//2)**2 -1
        c = b+2
    else:
        b = (a**2-1)//2
        c = b + 1

    return [a,b,c]
    # if a%2==0:#even
    #     mn = a//2
    #     l = list(range(1,10))
    #     for i in combinations(l, 2):
    #         m, n = i[0], i[1]
    #         if m*n == mn:
    #             break
    #     b = abs(m**2 - n**2)
    #     c = m**2 + n**2
    #     return [a, b, c]
    # else:
    #     l = list(range(1,10))
    #     for i in combinations(l, 2):
    #         m, n = i[0], i[1]
    #         print(m,n)
    #         if abs(m**2 - n**2) == a:
    #             break
    #     b = 2*m*n
    #     c = m**2 + n**2
    #     # k = ((a**2) - 1) // 2
    #     # b = k
    #     # c = k+1
    #     return [a,b,c]

a = int(input().strip())
triple = pythagoreanTriple(a)
print (" ".join(map(str, triple)))
