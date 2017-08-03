#!/bin/python3

import sys

def getGCD(a,b):
    if b!=0:
        return getGCD(b, a%b)
    else:
        return a

def maximumGcdAndSum(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    max_sum=1
    max_gcd=1
    for x in A:
        if x<=max_gcd:
            break
        for y in B:
            if y<=max_gcd:
                break
            gcd = getGCD(x, y)
            if gcd>max_gcd or (gcd==max_gcd and max_sum < x+y):
                max_gcd = gcd
                max_sum = x + y
    return max_sum

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B)
    print(res)
