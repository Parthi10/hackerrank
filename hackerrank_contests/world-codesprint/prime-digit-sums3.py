#!/bin/python3

import sys
from itertools import product
import time
primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
primeSet5_zero = [(0, 1, 1, 1, 0), (0, 1, 1, 0, 1), (0, 1, 2, 0, 0), (0, 2, 1, 2, 2), (0, 2, 1, 2, 8), (0, 2, 1, 2, 0), (0, 2, 1, 4, 6), (0, 2, 1, 4, 0), (0, 2, 1, 8, 2), (0, 2, 1, 8, 8), (0, 2, 1, 0, 2), (0, 2, 1, 0, 4), (0, 2, 3, 2, 6), (0, 2, 3, 2, 0), (0, 2, 3, 6, 2), (0, 2, 3, 6, 8), (0, 2, 3, 8, 6), (0, 2, 3, 8, 0), (0, 2, 3, 0, 2), (0, 2, 3, 0, 8), (0, 2, 3, 0, 0), (0, 2, 5, 4, 2), (0, 2, 5, 4, 8), (0, 2, 5, 6, 6), (0, 2, 5, 6, 0), (0, 2, 5, 0, 6), (0, 2, 5, 0, 0), (0, 2, 9, 2, 6), (0, 2, 9, 2, 0), (0, 2, 9, 6, 2), (0, 2, 9, 8, 0), (0, 2, 9, 0, 2), (0, 2, 9, 0, 8), (0, 2, 0, 1, 2), (0, 2, 0, 1, 4), (0, 2, 0, 3, 2), (0, 2, 0, 3, 8), (0, 2, 0, 3, 0), (0, 2, 0, 5, 6), (0, 2, 0, 5, 0), (0, 2, 0, 9, 2), (0, 2, 0, 9, 8), (0, 2, 0, 0, 3), (0, 2, 0, 0, 5), (0, 3, 2, 0, 0), (0, 3, 0, 2, 0), (0, 3, 0, 0, 2), (0, 4, 1, 2, 4), (0, 4, 1, 2, 0), (0, 4, 1, 6, 6), (0, 4, 1, 6, 0), (0, 4, 1, 8, 4), (0, 4, 1, 0, 2), (0, 4, 1, 0, 6), (0, 4, 3, 4, 6), (0, 4, 3, 4, 0), (0, 4, 3, 6, 4), (0, 4, 3, 0, 4), (0, 4, 3, 0, 0), (0, 4, 7, 2, 4), (0, 4, 7, 6, 6), (0, 4, 7, 6, 0), (0, 4, 7, 8, 4), (0, 4, 7, 0, 6), (0, 4, 7, 0, 0), (0, 4, 9, 4, 6), (0, 4, 9, 4, 0), (0, 4, 9, 6, 4), (0, 4, 9, 0, 4), (0, 5, 2, 0, 0), (0, 5, 0, 2, 0), (0, 5, 0, 0, 2), (0, 6, 1, 4, 2), (0, 6, 1, 4, 6), (0, 6, 1, 4, 8), (0, 6, 1, 4, 0), (0, 6, 1, 6, 4), (0, 6, 1, 6, 6), (0, 6, 1, 6, 0), (0, 6, 1, 0, 4), (0, 6, 1, 0, 6), (0, 6, 5, 2, 4), (0, 6, 5, 2, 6), (0, 6, 5, 2, 0), (0, 6, 5, 6, 2), (0, 6, 5, 6, 6), (0, 6, 5, 6, 0), (0, 6, 5, 8, 4), (0, 6, 5, 8, 0), (0, 6, 5, 0, 2), (0, 6, 5, 0, 6), (0, 6, 5, 0, 8), (0, 6, 5, 0, 0), (0, 6, 7, 4, 2), (0, 6, 7, 4, 6), (0, 6, 7, 4, 0), (0, 6, 7, 6, 4), (0, 6, 7, 6, 0), (0, 6, 7, 0, 4), (0, 6, 7, 0, 6), (0, 6, 7, 0, 0), (0, 8, 3, 2, 6), (0, 8, 3, 2, 0), (0, 8, 3, 6, 2), (0, 8, 3, 8, 0), (0, 8, 3, 0, 2), (0, 8, 3, 0, 8), (0, 8, 3, 0, 0), (0, 8, 5, 4, 2), (0, 8, 5, 6, 0), (0, 8, 5, 0, 6), (0, 8, 5, 0, 0), (0, 8, 9, 2, 0), (0, 8, 9, 6, 8), (0, 8, 9, 0, 2), (0, 9, 2, 0, 0), (0, 0, 2, 1, 2), (0, 0, 2, 1, 4), (0, 0, 2, 1, 8), (0, 0, 2, 1, 0), (0, 0, 2, 3, 2), (0, 0, 2, 3, 6), (0, 0, 2, 3, 8), (0, 0, 2, 3, 0), (0, 0, 2, 5, 4), (0, 0, 2, 5, 6), (0, 0, 2, 5, 0), (0, 0, 2, 9, 2), (0, 0, 2, 9, 6), (0, 0, 2, 9, 8), (0, 0, 2, 9, 0), (0, 0, 2, 0, 1), (0, 0, 2, 0, 3), (0, 0, 2, 0, 5), (0, 0, 2, 0, 9), (0, 0, 2, 0, 0), (0, 0, 3, 2, 2), (0, 0, 3, 2, 6), (0, 0, 3, 2, 8), (0, 0, 3, 2, 0), (0, 0, 3, 4, 4), (0, 0, 3, 4, 6), (0, 0, 3, 4, 0), (0, 0, 3, 8, 2), (0, 0, 3, 8, 6), (0, 0, 3, 8, 8), (0, 0, 3, 8, 0), (0, 0, 3, 0, 2), (0, 0, 3, 0, 4), (0, 0, 3, 0, 8), (0, 0, 3, 0, 0), (0, 0, 5, 2, 4), (0, 0, 5, 2, 6), (0, 0, 5, 2, 0), (0, 0, 5, 6, 2), (0, 0, 5, 6, 6), (0, 0, 5, 6, 8), (0, 0, 5, 6, 0), (0, 0, 5, 8, 4), (0, 0, 5, 8, 6), (0, 0, 5, 8, 0), (0, 0, 5, 0, 2), (0, 0, 5, 0, 6), (0, 0, 5, 0, 8), (0, 0, 5, 0, 0), (0, 0, 7, 4, 2), (0, 0, 7, 4, 6), (0, 0, 7, 4, 8), (0, 0, 7, 4, 0), (0, 0, 7, 6, 4), (0, 0, 7, 6, 6), (0, 0, 7, 6, 0), (0, 0, 7, 0, 4), (0, 0, 7, 0, 6), (0, 0, 7, 0, 0)]

def check(s,primeList,l):
    for i in range(l-2):
        num = sum(s[i:i+3])
        try:
            if num not in primeList:
                return False
            num += s[i+3]
            if num not in primeList:
                return False
            num += s[i+4]
            if num not in primeList:
                return False
        except:
            pass

    return True

intlist = [1,2,3,4,5,6,7,8,9,0]
numlist = product(intlist,repeat=3)
primeSet = []
for i in numlist:
    if i[0]!=0 and check(i,primeList,3):
        primeSet.append(i)
# print(primeSet)

q = int(input().strip())

for _ in range(q):
    n = int(input().strip())
    c = 0
    if n>=5:
        numlist = [x+i for x in primeSet5_zero for i in product(intlist, repeat=n-5)]
        l = len(numlist[0])
        for i in numlist:
            if check(i,primeList,l):
                c+=1
                print(i)
        print(c)