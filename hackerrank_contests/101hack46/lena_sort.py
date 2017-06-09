#!/bin/python3

import sys
import math


def lena_sort(arr, count=0):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = []
    more = []
    for i in arr:
        if i<pivot:
            count+=1
            less.append(i)
        else:
            more.append(i)

    sorted_less = lena_sort(less, count)
    sorted_more = lena_sort(more, count)
    ans = sorted_less + pivot + sorted_more

    return count

q = int(input().strip())
for a0 in range(q):
    len,c = input().strip().split(' ')
    len,c = [int(len),int(c)]
    #print(math.factorial(len-1))
    # your code goes here
    if math.factorial(len-1) >= c:
        for i in range(1, len+1):
            print(i, end=" ")

        print()

    else:
        print('-1')
