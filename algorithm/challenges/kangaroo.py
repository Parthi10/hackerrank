#!/bin/python3

import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

i, j = x1, x2
if (x2> x1 and v2 > v1) or (x1 > x2 and v1 > v2):
    print('NO')
elif (x1 > x2 and v1 < v2):
    y = x1 - x2
    x = v2 - v1
    if (y//x) * x == y:
        print('YES')
    else:
        print('NO')
else:
    y = x2 - x1
    x = v2 - v1
    if (y//x) * x == y:
        print("YES")
    else:
        print('NO')
