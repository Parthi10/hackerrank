#!/bin/python3

import sys
n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
s = input().strip()
for a0 in range(q):
    inp = [int(x) for x in input().strip().split(' ')]
    if inp[0] == 1:
        s = list(s)
        for i in range(inp[1],inp[2]+1):
            asc = ord(s[i]) + inp[3]
            if asc > 122:
                asc = 97 + (asc-122)
            s[i] = chr(asc)
        print(s)
    else:
        
