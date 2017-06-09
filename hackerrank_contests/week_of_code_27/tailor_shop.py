#!/bin/python3

import sys

n,p = input().strip().split(' ')#total no. of clusters, and cost per button
n,p = [int(n),int(p)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

clusterButtons = []
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
        noOfButtons += 1
        return addButtonToCluster(noOfButtons)
    else:
        clusterButtons.append(noOfButtons)
        return noOfButtons

ans = 0
for i in a:
    ans+=addCluster(i,p)
    # print(i,ans,clusterButtons)

print(ans)
