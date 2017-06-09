#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    s = [int(p_temp) for p_temp in input().strip().split(' ')]
    x = 0
    for i in s:
        x ^= i
    if x:
        if len(s)%2==0:
            print("W")
        else:
            print("L")
    else:#x=0
        if len(s)%2==0:
            print("L")
        else:
            print("W")
