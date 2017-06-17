#!/bin/python3

import sys

def solve(a, n): #O(n)
    if n==1: return 'YES'
    i = 0
    s1 = 0
    s2 = sum(a) - a[0]
    while i<n-1:
        if s1 == s2:
            return 'YES'
        else:
            s1 += a[i]
            i+=1
            s2 -= a[i]
    return 'NO'

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a, n)
    print(result)
