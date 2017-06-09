#!/bin/python3
import sys
n,q = input().strip().split(' ')
n,q = [int(n),int(q)]

'''
CORRRRECT SOLUTION
OKAY I GOT A PATTERN.. EVEN NO. OCCUR IN PATTERN.
2,4,5  9,11,12  16
'''
def check(i):
    rem = i%7
    if rem==2 or rem==4 or rem==5:
        return True
    else:
        return False
count90=0
count180=0
count270=0
ans = [0]
for i in range(1,n+1):
    for j in range(1,n+1):
        key = check((i*j)**2)
        key90 = check((j*(n+1-i))**2)
        key180 = check(((n+1-i)*(n+1-j))**2)
        key270 = check(((n+1-j)*i)**2)
        if key^key90:
            count90+=1
        if  key^key180:
            count180+=1
        if  key^key270:
            count270+=1

ans+=[count90,count180,count270]
# print(ans)
for a0 in range(q):
    angle = int(input().strip())
    print(ans[(angle%360)//90])
