#!/bin/python3

import sys

#as the range of n,m, x is very large, recursion will give error at large values of n,m
'''
def get_min_number(a, b, x, sum_so_far=0):
    if a[0] <= b[0] and sum_so_far+a[0]<x:
        sum_so_far += a.pop(0)
        return 1 + get_min_number(a, b, x, sum_so_far)
    elif b[0] < a[0] and sum_so_far+b[0]<x:
        sum_so_far += b.pop(0)
        return 1 + get_min_number(a, b, x, sum_so_far)
    return 0
'''

def get_prefix_sum(l):
    
g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    num_of_ints_removed_so_far = 0
    sum_so_far = 0
    while True:
        if sum_so_far <= x:
            if a[0] <= b[0] and sum_so_far+a[0]<=x:
                sum_so_far += a.pop(0)
                num_of_ints_removed_so_far += 1
            elif b[0] < a[0] and sum_so_far+b[0]<=x:
                sum_so_far += b.pop(0)
                num_of_ints_removed_so_far += 1
            else:
                print(num_of_ints_removed_so_far)
                break
        else:
            print(num_of_ints_removed_so_far)
            break
