#!/bin/python3

import sys
from collections import defaultdict

class Node(object):

    def __init__(self, data):
        self.parent = self
        self.rank = 0
        self.data = data

class DisjoinSetsContainer(object):

    def __init__(self):
        self.map = defaultdict(lambda:None) #gives set; given data. default is set to None

    def make(self, data):
        node = Node(data)
        self.map[data] = node
        return node

    def union(self, data1, data2):
        # print("got", data1, data2, self.disjointSetList)
        node1 = self.map[data1]
        node2 = self.map[data2]

        if not node1:
            node1 = self.make(data1)
        if not node2:
            node2 = self.make(data2)

        parent1 = self.find(data1)
        parent2 = self.find(data2)
        if parent1.data == parent2.data:
            return #both same, i.e, both nodes are in same set, no need of union

        #whoever's rank is higher, becomes parent of other
        if parent1.rank >= parent2.rank:
            if parent1.rank == parent1.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2


    def find(self, data): #there's a set with data: data
        node = self.map[data]
        node_parent = node.parent
        if node_parent.parent == node_parent:
            return node_parent

        #path compression, iteratively
        nodes_in_between = []
        while node != node.parent:
            nodes_in_between.append(node)
            node = node.parent

        for i in nodes_in_between:
            i.parent = node
        return node

def longest_pal(a, m, M):
    mat = [[0 for x in range(m)] for y in range(m)]
    for x in range(m):
        mat[x][x] = 1

    for l in range(2, m+1):
        for i in range(m-l+1):
            j = i + l - 1
            if (l==2 and M.find(a[i]).data==M.find(a[j]).data):
                mat[i][j] = 2
            elif M.find(a[i]).data==M.find(a[j]).data:
                a[i] = a[j]
                mat[i][j] = 2 + mat[i+1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i+1][j])
    # for i in mat:
    #     print(i)
    return mat[0][m-1]



M = DisjoinSetsContainer()
n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    M.union(x, y)
a = list(map(int, input().strip().split(' ')))
print(longest_pal(a, m, M))
