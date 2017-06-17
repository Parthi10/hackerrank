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

def find_path_dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for next_node in graph[start]:
        if next_node not in path:
            new_path = find_path_dfs(graph, next_node, end, path)
            if new_path:
                return new_path

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
    num = find_number_of_occurances(graph, u, v, p, s)
    print(num)
