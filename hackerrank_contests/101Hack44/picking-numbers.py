#!/bin/python3
'''
https://www.hackerrank.com/contests/101hack44/challenges/picking-numbers
'''
import sys
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
countArr = [0] * (max(a)+1)
for i in a:
    countArr[i]+=1
maxRepeatedNum = countArr.index(max(countArr))
ans = 2
for i in range(len(countArr)-1):
    adjacentSum = countArr[i]+countArr[i+1]
    if ans < adjacentSum:
        ans = adjacentSum

print(ans)
