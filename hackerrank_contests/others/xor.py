#!/bin/python3

import sys

'''
BRUTE FORCE METHOD


q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    a = 1
    count = 0
    while a < x:
        if (a ^ x) > x:
            count += 1
            print(a)
        a += 1
    print(count)
'''

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    binary_of_x = bin(x)[2:]
    y = len(binary_of_x)
    max_num = '1'*y #max bit value for same number of digits as binary_of_x
    max_num = int(max_num, 2)
    print(max_num-x)#why so?? the numbers which it can be equal to
    #to understand take example of 10, and plot all bin values from 1 to 10, observe!
