#!/bin/python3
#https://www.hackerrank.com/challenges/hackerland-radio-transmitters

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = sorted([int(x_temp) for x_temp in input().strip().split(' ')])

no_of_transmitters = 0
i = 0 #index
pointer = 0

while i<n:
    no_of_transmitters += 1
    pointer = x[i] + k
    while (i<n and x[i] <= pointer):
        i += 1
    pointer = x[i-1] + k
    while (i<n and x[i] <= pointer):
        i += 1
print(no_of_transmitters )
# for j in range(i+1, n):
#     if x[j] > x[i] + k:
#         pointer = j-1 +
#         transmitter += 1 # transmitter at x[j-1]
