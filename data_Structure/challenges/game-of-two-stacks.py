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


g = int(input().strip())
for a0 in range(g):
    n,m,max_sum = input().strip().split(' ')
    n,m,max_sum = [int(n),int(m),int(max_sum)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    ans = 0
    sum_so_far = 0
    i, j = 0,0
    while (i<n and sum_so_far + a[i] <= max_sum):
        sum_so_far += a[i]
        i += 1
    ans = i
    while (j<m and i>=0):
        sum_so_far += b[j]
        j+=1
        while(sum_so_far>max_sum and i>0):
            i -= 1
            sum_so_far -= a[i]
        if sum_so_far <= max_sum and ans < i+j:
            ans = i+j
        #optimise, prevent j to traverse the whole b stack, there's no need
        if i==0 and sum_so_far>max_sum:
            break
    print(ans)
