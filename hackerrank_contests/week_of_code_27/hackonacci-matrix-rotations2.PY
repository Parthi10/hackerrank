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
    # print("got",i)
    if i in hackonacciDictionary.keys():
        return hackonacciDictionary[i]
    else:
        #return hackonacci(i-1) + 2*hackonacci(i-2) + 3*hackonacci(i-3)
        hackonacciDictionary[i] = hackonacci(i-1) + 3*hackonacci(i-3)
        return hackonacciDictionary[i]
for i in range(4,n**4):
    hackonacciDictionary[i] = hackonacci(i)
originalMatrix = [['X' if hackonacci((x*y)**2)%2==0 else 'Y' for x in range(1,n+1)] for y in range(1,n+1)]

# newMatrix = [row[:] for row in originalMatrix]
# print(originalMatrix)
ans = [0]
#90 degreee count
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if originalMatrix[i-1][j-1] != originalMatrix[j-1][n-i]:
            count+=1
ans.append(count)
#180 degreee count
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if originalMatrix[i-1][j-1] != originalMatrix[n-i][n-j]:
            count+=1
ans.append(count)
#270 degreee count
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if originalMatrix[i-1][j-1] != originalMatrix[n-j][i-1]:
            count+=1
ans.append(count)

print(ans)
# for a0 in range(q):
#     angle = int(input().strip())
#     print(ans[angle//90])
