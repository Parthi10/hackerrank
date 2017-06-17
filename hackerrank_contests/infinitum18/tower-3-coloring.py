#!/bin/python3

import sys
from collections import defaultdict

# def binpow(a, b):
#     if b == 1:
#         return a
#     res = binpow(a, b // 2)
#     return res * res * (a if b % 2 != 0 else 1)

def binpow(a, b):
    res = 1
    cur = a
    while b > 0:
        if b & 1:
            res *= cur
        cur *= cur
        b >>= 1
    return res

def towerColoring(n):
    height = binpow(3, n)

    m = (10**9) +7
    print(height)
    
    height = height % m
    print(height)
    return binpow(3, height) % m

n = int(input().strip())
result = towerColoring(n)
print(result)
