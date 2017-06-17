#!/bin/python3

import sys
from collections import defaultdict
import re

def find_path_dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for next_node in graph[start]:
        if next_node not in path:
            new_path = find_path_dfs(graph, next_node, end, path)
            if new_path:
                return new_path

def number_of_occurances(s, p, path):
    m = len(p)
    count = 0
    # print(path)
    for i in range(len(path)):
        # print([s[x-1] for x in path[i:i+m]], i, p)
        if [s[x-1] for x in path[i:i+m]] == p:
            count+=1
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

for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    path = find_path_dfs(graph, u, v)

    print(number_of_occurances(s,p, path))
