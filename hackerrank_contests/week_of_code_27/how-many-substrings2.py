#!/bin/python3
from itertools import combinations as combo
import sys
import os

def countDistinctSubstrings(string):
    # print(string)
    suffix_array = sorted([string[i:] for i in range(n)])
    suffix_array_pair = [suffix_array[i:i+2] for i in range(n-1)]
    ans=len(suffix_array_pair[0][0])
    for i in suffix_array_pair:
        ans += len(i[1]) - len(os.path.commonprefix(i))
    return ans


n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
s = input().strip()
for a0 in range(q):
    left,right = input().strip().split(' ')
    left,right = [int(left),int(right)]
    string = s[left:right+1]
    count = countDistinctSubstrings(string)
    print(count)


'''
6 1
BANANA
0 6

'''
