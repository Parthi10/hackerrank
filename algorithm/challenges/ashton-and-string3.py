#!/bin/python3
from itertools import combinations as combo
import sys
import os

def countDistinctSubstrings(string):
    # print(string)
    n = len(string)
    suffix_array = sorted([string[i:] for i in range(n)])
    suffix_array_pair = [suffix_array[i:i+2] for i in range(n-1)]
    print(suffix_array,suffix_array_pair)
    for i in suffix_array_pair:
        print(os.path.commonprefix(i))

t = int(input().strip())

for _ in range(t):
    string = input().strip()
    k = int(input().strip())
    # substrings = ([string[i:j] for i,j in combo(range(len(string)+1),2)])
    # ans = "".join(substrings)
    # print(ans[k-1])
    countDistinctSubstrings(string)
