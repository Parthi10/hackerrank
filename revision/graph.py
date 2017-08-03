from collections import defaultdict
graph = {
        1: [2, 3],
        2: [1, 3, 4, 7],
        3: [1, 2, 4],
        4: [2, 3],
        5: [6, 7],
        6: [5],
        7: [2, 5]
    }
'''
traverse the graph starting from 'start' node
'''
#loop, non-recursive,
def dfs1(graph, start):
    path = [start]
    stack = [start]
    visited = defaultdict(lambda:False)
    visited[start] = True
    while stack:
        node = stack.pop()
        for neighbour in graph[node]:
            if not visited[neighbour]:
                stack.append(neighbour)
                path.append(neighbour)
                visited[neighbour] = True
    return path

#print(dfs1(graph, 2))

# recursive
def dfs2(graph, start, visited):
    path = [start]
    visited[start] = True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            path += dfs2(graph, neighbour, visited)
    return path

#visited = defaultdict(lambda:False)
#print(dfs2(graph, 2, visited))

#loop, non-recursive
def bfs1(graph, start):
    visited = defaultdict(lambda:False)
    visited[start] = True
    path = [start]
    queque = [start]
    while queque:
        node = queque.pop(0)
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queque.append(neighbour)
                path.append(neighbour)
    return path

# print(bfs1(graph, 2))

'''
Shortest path between `start` and `end`
'''

def getPathFromParentDict(parent, start, end):
    path = [end]
    while True:
        path.append(parent[end])
        end = parent[end]
        if end == start:
            return path

#shortest path, works on cyclic graphs too!, as bfs is level wise traversal.
def bfs(graph, start, end):
    parent = defaultdict(lambda:None)#to store parents of nodes in traversal
    queque = [start]
    while queque:
        node = queque.pop(0)
        for neighbour in graph[node]:
            if not parent[neighbour]:
                parent[neighbour] = node
                queque.append(neighbour)
                if neighbour == end:#generate path
                    return getPathFromParentDict(parent, start, end)

#print(bfs(graph, 4, 6))

def dfs(graph, start, end):
    stack = [start]
    parent = defaultdict(lambda:None)
    while stack:
        node = stack.pop()
        for neighbour in graph[node]:
            if not parent[neighbour]:
                parent[neighbour] = node
                stack.append(neighbour)
                if neighbour == end:
                    return getPathFromParentDict(parent, start, end)

# print(bfs(graph, 4, 1))

'''
Get all possible paths
'''
def bfsGetAllPaths(graph, start, end):
    paths = []
    queque = [[start]]
    while queque:
        temp_path = queque.pop(0)
        node = temp_path[-1]
        if node==end:
            paths.append(temp_path)
        for neighbour in graph[node]:
            if neighbour not in temp_path:
                new_path = temp_path + [neighbour]
                queque.append(new_path)
    return paths

# print(bfsGetAllPaths(graph, 2, 3))

def dfsGetAllPaths(graph, start, end):
    paths = []
    stack = [[start]]
    while stack:
        temp_path = stack.pop()
        node = temp_path[-1]
        if node==end:
            paths.append(temp_path)
        for neighbour in graph[node]:
            if neighbour not in temp_path:
                new_path = temp_path + [neighbour]
                stack.append(new_path)
    return paths

# print(dfsGetAllPaths(graph, 3, 5))


'''
Mark connected componensts
'''

graph2 = {
        1: [2, 3],
        2: [1, 3, 4, 7],
        3: [1, 2, 4],
        4: [2, 3],
        8: [9],
        5: [6],
        6: [5],
        7: [2],
        9: [8]
    }

def mark_nodes_dfs(graph, node, mark, mark_dict):
    stack = [node]
    while stack:
        node = stack.pop()
        mark_dict[node] = mark
        for neighbour in graph2[node]:
            if not mark_dict[neighbour]:
                stack.append(neighbour)


mark_dict = defaultdict(int)
mark = 1
for node in graph2:
    if not mark_dict[node]:
        mark_nodes_dfs(graph2, node, mark, mark_dict)
        mark += 1
print(dict(mark_dict))

'''
Dijkstra's Algorithm, shortest path
'''

#Using MinHeapMap DS
from heapq import heapify, heappush, heappop

class Node(object):
    def __init__(self, weight, key):
        self.weight = weight
        self.key = key

class MinHeap(object):
    def __init__(self):
        self.heap = []
        self.map = defaultdict(lambda:None)#{key of node:index in heap list}

    def insert(self, weight, key):
        self.heap.append(Node(weight, key))
        self.map[key] = len(self.heap) - 1
        self.fixTheHeap(self.map[key])

    def getParent(self, i):
        return (i-1) // 2

    def fixTheHeap(self, index):
        node = self.heap[index]
        parent = self.getParent(index)

class Graph(object):
    def __init__(self):
        self.map = defaultdict(dict)

    def addEdge(self, u, v, w):
        self.map[u][v] = w
        self.map[v][u] = w

graph = Graph()

graph.addEdge('A', 'B', 3)
graph.addEdge('B', 'C', 1)
graph.addEdge('C', 'A', 1)
graph.addEdge('A', 'D', 1)
graph.addEdge('B', 'D', 3)
graph.addEdge('D', 'E', 6)
graph.addEdge('E', 'F', 2)
graph.addEdge('C', 'E', 5)
graph.addEdge('C', 'F', 4)

vertices = ['A', 'B', 'C', 'D', 'E', 'F']



'''
O(n) without heap
'''
class Graph(object):
    def __init__(self):
        self.map = defaultdict(dict)

    def addEdge(self, u, v, w):
        self.map[u][v] = w
        self.map[v][u] = w

    def getMin(self, distMap):
        min_weight = float('inf')
        print(dict(distMap))
        for neighbour, weight in distMap.items():
            if weight<min_weight:
                min_weight = weight
                node = neighbour
        return node

    def dijkstra(self, source):
        distMap = defaultdict()
        for vertex in self.map:
            distMap[vertex] = float('inf')
        distMap[source] = 0

        vertexToParent = defaultdict(lambda:None)
        distanceFromStartVertex = defaultdict()

        while bool(distMap):#notEmpty on heap
            node = self.getMin(distMap)#extracMin on heap O(1), O(n) here
            distanceFromStartVertex[node] = distMap[node]
            del distMap[node]#deleteKey on heap O(logN), here O(1)
            for neighbour, weight in self.map[node].items():
                try:
                    distMap[neighbour]#check if neighbour is in distMap
                    distance = distanceFromStartVertex[node] + weight
                    if distMap[neighbour] > distance:
                        distMap[neighbour] = distance
                        vertexToParent[neighbour] = node
                except:
                    pass

        print(dict(vertexToParent))
        print(dict(distanceFromStartVertex))

graph = Graph()

graph.addEdge('A', 'B', 3)
graph.addEdge('B', 'C', 1)
graph.addEdge('C', 'A', 1)
graph.addEdge('A', 'D', 1)
graph.addEdge('B', 'D', 3)
graph.addEdge('D', 'E', 6)
graph.addEdge('E', 'F', 2)
graph.addEdge('C', 'E', 5)
graph.addEdge('C', 'F', 4)
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

graph.dijkstra('A')
