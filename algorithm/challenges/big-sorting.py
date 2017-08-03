#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)

def merge(L, R, array):
    nL, nR = len(L), len(R)
    l, r, i = 0, 0, 0

    while l<nL and r<nR:
        if len(L[l])<len(R[r]) or (len(L[l]) == len(R[r]) and L[l] < R[r]):
            array[i] = L[l]; l += 1
        else:
            array[i] = R[r]; r += 1
        i+=1

    while l<nL:
        array[i] = L[l]
        l+=1; i+=1

    while r<nR:
        array[i] = R[r]
        r+=1; i+=1

    return array

def merge_sort(array):
    if len(array)==1:
        return array
    L = array[:len(array)//2]
    R = array[len(array)//2:]
    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R, array)

for i in merge_sort(unsorted):
    print(i)
