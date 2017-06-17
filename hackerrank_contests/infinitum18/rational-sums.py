#!/bin/python3

import sys
from fractions import Fraction

def rationalSums(n, a, b):
    ans = 0
    for x in range(1, n+1):
        p = b[0] + sum([x*bi for bi in b[1:]])
        q = 1
        for ai in a:
            q *= (x+ai)
        ans += Fraction(p, q)
    return ans
    
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
result = rationalSums(n, a, b)
print(result)
