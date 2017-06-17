#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    a1 = min(ar1)
    a2 = min(ar2)
    if ar1.index(a1) != ar2.index(a2):
        return a1+a2
    else:
        a = sorted(ar1)
        b = sorted(ar2)
        if a[1] < b[1]:
            return a[1] + a2
        else:
            return a1 + b[1]


n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)
