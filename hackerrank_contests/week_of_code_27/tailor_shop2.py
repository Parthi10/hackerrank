#!/bin/python3

import sys

n,p = map(int, input().strip().split(' '))


clusterButtons = [0] #to store already addded noOfButtons to clusters
def addCluster(clusterCost,buttonCost):
    noOfButtons = clusterCost//buttonCost
    if clusterCost%buttonCost != 0:
        noOfButtons += 1
    elif clusterCost == 0:#wants to spend atleast 0 on this cluster
        noOfButtons = 1
    return addButtonToCluster(noOfButtons)

#given noOfButtons add it to cluster,.increase it if already same noOfButtons add in cluster
def addButtonToCluster(noOfButtons):
    if noOfButtons in clusterButtons:
        noOfButtons = max(clusterButtons) + 1
    clusterButtons.append(noOfButtons)
    return noOfButtons

ans = 0
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for i in sorted(a, reverse=True):
    ans+=addCluster(i,p)
    # print(i,ans,clusterButtons)

print(ans)
