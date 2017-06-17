#!/bin/python3

import sys
from collections import defaultdict

class Graph(object):
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.paths = set()

    def set_positions(self, u=None, v=None, w=None):
        self.u = None
        self.v = None
        self.w = None

    def add_edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    #DFS
    def get_all_possible_paths(self, start, end, path=[]):
        path = path + [start]

        if start==end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.get_all_possible_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths


n, m, q = input().strip().split(' ')
n, m, q = [int(n), int(m), int(q)]
G = Graph(n)
for a0 in range(m):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    G.add_edges(u, v)

for a0 in range(q):
    u, v, w = input().strip().split(' ')
    u, v, w = [int(u), int(v), int(w)]
    print(G.get_all_possible_paths(u, w))

'''
4 4 1
1 2
2 3
2 4
3 1
2 4 2
'''
