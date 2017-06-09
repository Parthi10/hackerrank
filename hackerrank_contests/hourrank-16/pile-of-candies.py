#!/bin/python3

import sys
n = int(input())
arr = [int(x) for x in input().strip().split(' ')]
min_num = min(arr)
min_num_count = arr.count(min_num)
min_num_index = arr.index(min_num)
new_arr = arr[:]
new_arr[min_num_index] *= 2
if new_arr[min_num_index] ==  min(new_arr):
    print(2*min_num, end=' ')
    print(min_num_count)
else:
    print(min(arr), arr.count(min(arr)))
