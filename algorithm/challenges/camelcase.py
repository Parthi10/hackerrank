#!/bin/python3

import sys

count = 0
s = input().strip()
for i in s:
    if ord(i)<=90:
        count+=1
        
print(count+1)