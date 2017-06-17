#!/bin/python3

import sys
from collections import defaultdict

class Graph(object):
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(set)

    def add_edges(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def dfs_paths(self, start, goal):
        all_paths = list()
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in self.graph[vertex] - set(path):
                if next == goal:
                    all_paths.append(path + [next])
                else:
                    stack.append((next, path + [next]))
        if len(all_paths) == 0 and start!=goal:
            return "NO PATH"
        return all_paths

    def bfs_paths(self, start, goal):
        all_paths = list()
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in self.graph[vertex] - set(path):
                if next == goal:
                    all_paths.append(path + [next])
                else:
                    queue.append((next, path + [next]))
        return all_paths

    def find_all_paths_bfs(self, start1, start2, end):
        valid_paths1, valid_paths2 = [], []

        stack1, stack2 = [], []
        temp_path1 = [start1]
        temp_path2 = [start2]
        stack1.append(temp_path1)
        stack2.append(temp_path2)
        while stack1 and stack2:
            temp_path1 = stack1.pop(0)
            temp_path2 = stack2.pop(0)
            last_node1 = temp_path1[-1]
            last_node2 = temp_path2[-1]

            if last_node1==end:
                valid_paths1.append(temp_path1)
                # print("1")
                if get_ans(temp_path1, valid_paths2):
                    # print(temp_path1, valid_paths2)
                    return "YES"
            if last_node2==end:
                valid_paths2.append(temp_path2)
                # print("2")
                if get_ans(temp_path2, valid_paths1):
                    # print(temp_path2, valid_paths1)
                    return "YES"
            for i in self.graph[last_node1]:
                if i not in temp_path1:
                    new_path1 = temp_path1 + [i]
                    stack1.append(new_path1)

            for i in self.graph[last_node2]:
                if i not in temp_path2:
                    new_path2 = temp_path2 + [i]
                    stack2.append(new_path2)

        return "NO"
def get_ans(new_path, paths2):
    # print("got", new_path, paths2)
    if paths2==[]:
        return False
    for path in paths2:
        flag = True
        for node in new_path[:-1]:
            if node in path:
                # print("breaking")
                flag = False
                break
        if flag:
            return True
    # print("flag", flag)
    return False



def get_final_answer(u, v, w):
    if u==v==w:
        return "YES"
    elif u==w:
        if len(G.bfs_paths(v, w))==0:
            return "NO"
        else:
            return "YES"
    elif v==w:
        if len(G.bfs_paths(u, w)) == 0:
            return "NO"
        else:
            return "YES"
    else:
        return G.find_all_paths_bfs(u,v,w)


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
    # print(get_ans(u, v, w))
    print(get_final_answer(u,v,w))



'''
4 4 1
1 2
2 3
2 4
3 1
2 4 1


7 8 1
1 2
2 4
4 7
2 5
1 3
3 5
5 6
5 7
2 3 2
'''
