#!/bin/python3

import sys
from itertools import product, combinations_with_replacement, permutations

def permutation_check(list):
    permu = combinations(list, len(list))
    ans = 0
    for i in permu:
        print("ho", i)
        if check(i, d):
            ans += 1
            print("got", i)
    return ans

def check(l, d):
    for i in range(len(l)):
        if l[i] - l[i-1] > d:
            return False
    return True


def numberOfLists(s, m, d):
    d_list = [x for x in range(0, d+1)] #permissible difference
    num_list = [x for x in range(1, m+1)] #permissible numbers
    ans = 0
    for z in range(1, s):
        l = combinations_with_replacement(num_list, z)
        for i in l:
            print(i)
            if sum(i) == s:
                if check(i,  d):
                    print("checking", i)
                    ans += permutation_check(i)
            elif sum(i) > s:
                break
    return ans+1



#  Return the number of lists satisfying the conditions above, modulo 1000000009.
s, m, d = input().strip().split(' ')
s, m, d = [int(s), int(m), int(d)]
result = numberOfLists(s, m, d)
print(result)
