#!/bin/python3
from collections import defaultdict

import sys

def dfs(graph, start):
    visited[start] = True
    count = 1
    for adjNode in graph[start]:
        if not visited[adjNode]:
            visited[adjNode] = True
            count += dfs(graph, adjNode)
    return count

q = int(input().strip())
for a0 in range(q):
    graph = defaultdict(set)
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    if x <= y:
        for a1 in range(m):
            input()
        print(x * n)
    else:
        for a1 in range(m):
            city_1, city_2 = input().strip().split(' ')
            city_1, city_2 = [int(city_1), int(city_2)]
            graph[city_1].add(city_2)
            graph[city_2].add(city_1)

        visited = defaultdict(lambda:False)
        groups = 0
        ans = 0
        totalConnectedOnes = 0
        for node in graph:
            if not visited[node]:
                size = dfs(graph, node)
                totalConnectedOnes += size
                groups += 1
        ans += (totalConnectedOnes - groups) * y #repair roads, one less than number of connected components in a groups
        ans += (n - totalConnectedOnes + groups )* x #a library in each connected component
        print(ans)
