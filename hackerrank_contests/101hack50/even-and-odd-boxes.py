#!/bin/python3

import sys

#extra_choc 0 1
def minimumChocolateMoves(n, X, start=0, flag=True, extra_choc=0):
    transfers = 0
    if start==n:
        return 0
    while start<n:
        print("Got start", start, transfers)
        if flag:#requires even
            if X[start]%2:#it is odd
                print(flag, X[start])
                if extra_choc:
                    extra_choc -= 1
                    X[start+1] += 1
                else:
                    extra_choc += 1
                    X[start+1] -= 1
                transfers+=1
            flag = False
        else: #requires odd
            if not X[start]%2:#it is even
                print(flag, X[start])
                if extra_choc:#there is extra_choc
                    extra_choc -= 1 #take one out of extra_choc and give it to the box to make it odd
                else:
                    extra_choc += 1 #take one out of box
                transfers+=1
            #if already odd, then pass
            flag=True
        start+=1

    return transfers

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
'''
