from collections import defaultdict
class Node(object):
    def __init__(self, name):
        self.name = name
        self.connections = defaultdict(int)


class Graph(object):
    def __init__(self):
        self.map = defaultdict(lambda:None)

    def addEdge(self, u, v, w):
        if not self.map[u]:
            self.map[u] = Node(u)
        if not self.map[v]:
            self.map[v] = Node(v)
        self.map[u].connections[self.map[v]] = r
        self.map[v].connections[self.map[u]] = r
