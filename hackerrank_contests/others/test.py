#!/bin/python3
from itertools import combinations as combo
from math import factorial as fac
import sys

n = int(input().strip())
number = input().strip()
number = list(str(number))
count = number.count('8')

try:
    for i in combo(number, 2):
        if int("".join(i)) % 8 == 0:
            count += 1


    for i in combo(number, 3):
        if int("".join(i)) % 8 == 0:
            x = number.index(i[0])
            if x:
                count += fact(x) + 1
            else:
                count +=1
except:
    pass
m = 10**9 + 7
print(count % m)
