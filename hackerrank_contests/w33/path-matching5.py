#!/bin/python3

import sys
from collections import defaultdict


def match(path, p, s):
    if len(p)>len(path):
        # print("lenp less than path, returning 0 as count")
        return 0
    # print("Got path, s_dash, p",path, s_dash, p)
    for i, j in enumerate(path):
        if s[j-1]!=p[i]:
            return 0
    return 1

def find_number_of_occurances(graph, start, end, p, s):
    len_p = len(p)
    tempPath = [start]
    count = 0
    stack = [[tempPath, count]]
    while stack:
        # print("\n stack: ", stack)
        tempPath, count = stack.pop(0)
        lastNode = tempPath[-1]

        count += match(tempPath[-len_p:], p, s)
        if lastNode == end:
            # print("VP", tempPath, count, p)
            # print("returning count")
            return count
        # flag=True
        for adjNode in graph[lastNode]:
            if adjNode not in tempPath :
                # print("adjNode", adjNode)
                # flag=False
                newPath = tempPath + [adjNode]
                stack.append([newPath, count])
        # print("flag", flag)

    return count

graph = defaultdict(list)

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
s = input().strip()
p = list(input().strip())
for a0 in range(n-1):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    graph[u].append(v)
    graph[v].append(u)

mat = [[None for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = find_number_of_occurances(graph, i+1, j+1, p, s)

for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    print(mat[u-1][v-1])
