#!/bin/python3
import sys
from collections import defaultdict

n,q = input().strip().split(' ')
n,q = [int(n),int(q)]

hackonacciDictionary = defaultdict(int)
hackonacciDictionary = {0:0,1:1,2:2,3:3}
def hackonacci(i):
    if i in hackonacciDictionary.keys():
        return hackonacciDictionary[i]
    else:
        hackonacciDictionary[i] = hackonacci(i-1) + 3*hackonacci(i-3)
        return hackonacciDictionary[i]

ans = [0]
limit = n**4 #if n**4>1000 else n**4 - 1000
for i in range(4, limit):
    hackonacciDictionary[i] = hackonacci(i)

count90=0
count180=0
count270=0
for i in range(1,n+1):
    for j in range(1,n+1):
        rem = hackonacciDictionary[(i*j)**2]%2
        if  rem != hackonacciDictionary[(j*(n+1-i))**2]%2:
            count90+=1
        if rem != hackonacciDictionary[((n+1-i)*(n+1-j))**2]%2:
            count180+=1
        if rem != hackonacciDictionary[((n+1-j)*(i))**2]%2:
            count270+=1

ans+=[count90,count180,count270]
print(ans)
for a0 in range(q):
    angle = int(input().strip())
    print(ans[(angle%360)//90])
