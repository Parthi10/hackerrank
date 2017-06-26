#!/bin/python3

import sys

#extra_choc 0 1
def minimumChocolateMoves(n, X):
    X = [x%2 for x in X]
    odds, evens = 0,0
    for i in range(n):
        if i%2 and not X[i]%2:#odd place even no
            odds +=1
        elif not i%2 and X[i]%2:#even place odd no.
            evens +=1

    if odds==evens:
        return odds
    else:
        return -1

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    X = list(map(int, input().strip().split(' ')))
    result = minimumChocolateMoves(n, X)
    print(result)
'''
1
6
6 8 3 1 1 4

1
5
3 1 1 1 1
'''
