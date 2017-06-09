#!/bin/python3

import sys
from itertools import product, combinations_with_replacement




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
        l = product(num_list, repeat=z)
        for i in l:
            if sum(i) == s:
                if check(i,  d):
                    ans +=1
                    # print(i)
            elif sum(i) > s:
                print(i)
                break
    return ans+1



#  Return the number of lists satisfying the conditions above, modulo 1000000009.
s, m, d = input().strip().split(' ')
s, m, d = [int(s), int(m), int(d)]
result = numberOfLists(s, m, d)
print(result % 1000000009)
