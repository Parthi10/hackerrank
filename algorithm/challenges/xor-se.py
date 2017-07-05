#!/bin/python3

import sys
a = [0]
for x in range(1, 200):
    newTerm = x ^ a[x-1]
    a.append(newTerm)

for x, y in enumerate(a):
    print(x, y)
# Q = int(input().strip())
# for a0 in range(Q):
#     L,R = input().strip().split(' ')
#     L,R = [int(L),int(R)]
