#!/bin/python3
import sys
s = input().strip()
n = int(input().strip())
ans = s.count('a')
if ans == 0:
    print(0)
else:
    ans = ( n//len(s) ) * ans
    rem = n%len(s)
    if rem != 0:
        ans += s[:n%len(s)].count('a')
    print(ans)
