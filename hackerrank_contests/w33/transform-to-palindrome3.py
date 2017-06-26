#!/bin/python3
'''
Passes all test cases
'''
import sys
from collections import defaultdict

def dfs(graph, start, mark, cc):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            mark[vertex] = cc
            visited.add(vertex)
            stack.extend(x for x in graph[vertex] if x not in visited)

def longest_pal(a, m, mark):
    mat = [[0 for x in range(m)] for y in range(m)]
    for x in range(m):
        mat[x][x] = 1

    for l in range(2, m+1):
        for i in range(m-l+1):
            j = i + l - 1
            if (l==2 and (mark[a[i]] == mark[a[j]])):
                a[i] = a[j]
                mat[i][j] = 2
            elif mark[a[i]] == mark[a[j]]:
                a[i] = a[j]
                mat[i][j] = 2 + mat[i+1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i+1][j])

    return mat[0][m-1]


graph = defaultdict(list)

n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    graph[x].append(y)
    graph[y].append(x)


a = list(map(int, input().strip().split(' ')))
mark = [None] * (n+1)

cc = 1
for i in range(n):
    if not mark[i]:
        dfs(graph, i, mark, cc)
        cc += 1
# print(mark)
print(longest_pal(a, m, mark))
