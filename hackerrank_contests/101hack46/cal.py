#!/bin/python3

import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
distance = 0
j = 0
calories = sorted(calories, reverse=True)
# print(calories)
for i in range(n):

    cal = calories[i]
    distance += (2**j) * cal
    j += 1
    
print(distance)

#print(distance)
# your code goes here

