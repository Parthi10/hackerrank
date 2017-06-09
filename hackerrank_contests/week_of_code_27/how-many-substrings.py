#!/bin/python3
from itertools import combinations as combo
import sys
'''
MY SOLUTION,..WORKS FOR 50%  CASES
'''

n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
s = input().strip()
for a0 in range(q):
    left,right = input().strip().split(' ')
    left,right = [int(left),int(right)]
    string = s[left:right+1]
    # substrings = ([string[i:j] for i,j in combo(range(len(string)+1),2)])
    substrings = []
    count = 0
    for i,j in combo(range(right-left+2),2):
        subs = string[i:j]
        if subs not in substrings:
            substrings.append(subs)
            count += 1
    print(count)
