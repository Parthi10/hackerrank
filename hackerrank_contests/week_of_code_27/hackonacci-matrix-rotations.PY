#!/bin/python3
import sys
from collections import defaultdict

n,q = input().strip().split(' ')
n,q = [int(n),int(q)]

'''
We need to check if even or odd, so neglect 2*hackonacci(i-2) as it is going to be even in either case
'''
hackonacciDictionary = defaultdict(int)
hackonacciDictionary = {0:0,1:1,2:2,3:3}
def hackonacci(i):
    if i in hackonacciDictionary.keys():
        return hackonacciDictionary[i]
    else:
        #return hackonacci(i-1) + 2*hackonacci(i-2) + 3*hackonacci(i-3)
        hackonacciDictionary[i] = hackonacci(i-1) + 3*hackonacci(i-3)
        return hackonacciDictionary[i]
originalMatrix = [['X' if hackonacci((x*y)**2)%2==0 else 'Y' for x in range(1,n+1)] for y in range(1,n+1)]
# newMatrix = [row[:] for row in originalMatrix]
# print(originalMatrix)

def countTheDifferences(times):
    count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if originalMatrix[i-1][j-1] != originalMatrix[j-1][n-i]:
                count+=1
    print(count)
    
'''
90 degrees --> times:1
180 degrees --> times:2
270 degrees --> times:3
'''

# for a0 in range(q):
#     angle = int(input().strip())
#
    # your code goes here
