#!/bin/python3
'''
CORRECT SOLUTION
'''
import sys

n,p = input().strip().split(' ')#total no. of clusters, and cost per button
n,p = [int(n),int(p)]

lastAddedButtons = 0
def addCluster(clusterCost,buttonCost):
    global lastAddedButtons
    # print("got", lastAddedButtons, clusterCost, buttonCost)
    noOfButtons = clusterCost//buttonCost

    if clusterCost%buttonCost != 0:
        noOfButtons += 1
    elif clusterCost == 0:
        noOfButtons = 1

    if noOfButtons > lastAddedButtons:
        lastAddedButtons = noOfButtons
    else:
        lastAddedButtons += 1
        noOfButtons = lastAddedButtons
    return noOfButtons



a = [int(a_temp) for a_temp in input().strip().split(' ')]
ans = 0
for i in sorted(a):
    ans+=addCluster(i,p)

    # print(i,ans,clusterButtons)

print(ans)
