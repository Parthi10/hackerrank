#!/bin/python3

import sys

#extra_choc 0 1
def minimumChocolateMoves(n, X, start=0, flag=True, extra_choc=0):
    print('Got', start, "extra_choc", extra_choc)
    transfers = 0
    if start==n:
        # if extra_choc
        return 0
    if flag:#requires even
        if X[start]%2:#it is odd
            print(flag, X[start])
            if extra_choc :
                extra_choc -= 1
            else:
                if X[start]>1:
                    extra_choc += 1
            transfers+=1
        flag = False
    else: #requires odd
        if not X[start]%2:#it is even
            print(flag, X[start])
            if extra_choc and X[start]>1:#there is extra_choc
                extra_choc -= 1 #take one out of extra_choc and give it to the box to make it odd
            else:
                if X[start]>1:
                    extra_choc += 1 #take one out of box
            transfers+=1
        #if already odd, then pass
        flag=True
    start+=1
    transfers += minimumChocolateMoves(n,X,start,flag,extra_choc)

    return transfers

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    X = list(map(int, input().strip().split(' ')))
    result = minimumChocolateMoves(n, X)
    print(result//2)

'''
1
6
6 8 3 1 1 4

1
5
3 1 1 1 1
'''
