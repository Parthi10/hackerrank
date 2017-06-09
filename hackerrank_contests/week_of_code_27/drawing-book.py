#!/bin/python3

import sys

n = int(input().strip())
p = int(input().strip())

if p==1 or p==n or p==n-1:
    print(0)
else:
    x = 2
    pageList = []
    while x<n-1:
        pageList.append([x,x+1])
        x+=2
    forward = 1
    # print(pageList)
    for i in pageList:
        if p in i:
            break
        forward+=1
    # print("forward", forward)
    if forward <= len(pageList)//2:
        print(forward)
    else:
        print(len(pageList)-forward +1)
