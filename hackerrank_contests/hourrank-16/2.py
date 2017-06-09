#!/bin/python3

import sys

# l = [4,7,11,16,49, 53, 23, 64, 65]
l=[]
for i in range(26):
    l.append(i*4)
for j in range(15):
    l.append(7*j)
q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    if n in l:
        print("Yes")
    else:
        print("No")
