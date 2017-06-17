#!/bin/python3

import sys

def check(s):
    for i in range(len(s)):
        if s[i] == '1':
            return True
        elif s[i] == '0':
            return check(s[i+1:])

        else:
            return False

def patternCount(s):
    n = len(s)
    i = 0
    ans = 0
    while i<n-2:
        if s[i] == '1' and s[i+1] =='0':
            if check(s[i+2:]):
                ans+=1
        i+=1
    return ans

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
