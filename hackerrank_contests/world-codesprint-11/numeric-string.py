#!/bin/python3

import sys

def get_base_10(substrings, k, b):
    ret = []
    for i in substrings:
        sum = 0
        for index, j in enumerate(reversed(i)):
            sum += j * (b**index)
        ret.append(sum)
    return ret

def getMagicNumber(s, k, b, m):
    l = len(s)
    substrings = [s[n:n+k] for n in range(l-k+1)]
    base_10_numbers = get_base_10(substrings,k, b)
    return sum([i%m for i in base_10_numbers])

s = list(map(int, list(input().strip())))
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
