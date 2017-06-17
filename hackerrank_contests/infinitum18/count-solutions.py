#!/bin/python3

import sys
from math import sqrt, ceil

def countSolutions(a, b, c, d):
    ans = 0
    radius_squared = (a**2 + b**2)/4
    if c==a and d==b:
        return 1
    elif c<a and d<b:
        return 0
    else:
        for x in range(1, c+1):
            x_term = radius_squared - ((x - a/2)**2)
            if x_term>=0:
                y1 = b/2 + sqrt(x_term)
                y2 = b/2 - sqrt(x_term)
                if y1 == y2 and y1.is_integer() and y1>=1 and y1<=d:
                    ans+=1
                else:
                    if y1.is_integer() and y1<=d and y1>=1:
                        ans+=1
                    if y2.is_integer() and y2<=d and y2>=1:
                        ans+=1
        return ans


q = int(input().strip())
for a0 in range(q):
    a, b, c, d = input().strip().split(' ')
    a, b, c, d = [int(a), int(b), int(c), int(d)]
    result = countSolutions(a, b, c, d)
    print(result)


'''
sample tc
4
10 12 50 50
10 23 50 50
51 11 50 50
51 11 19 50

3 3 2 0
'''
