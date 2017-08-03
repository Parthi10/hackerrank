from collections import defaultdict

class Node(object):

    def __init__(self, data):
        self.parent = self
        self.rank = 0
        self.data = data

class DisjoinSetsContainer(object):

    def __init__(self):
        self.map = defaultdict(lambda:None) #gives node; given data. default is set to None

    def make(self, data):
        node = Node(data)
        self.map[data] = node
        return node

    def union(self, data1, data2):
        # print("got", data1, data2, self.disjointSetList)
        node1 = self.map[data1]
        node2 = self.map[data2]

        parent1 = self.find(data1)
        parent2 = self.find(data2)
        if parent1 == parent2:
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

        #path compression recursively, will give runtime error in large test case
        node.parent = self.find(node.parent.data)
        return node.parent

        '''
        #path compression, iteratively
        nodes_in_between = []
        while node != node.parent:
            nodes_in_between.append(node)
            node = node.parent

        if nodes_in_between:
            for i in nodes_in_between:
                i.parent = node
        return node
        '''

graph = defaultdict(lambda:float('inf'))

M = DisjoinSetsContainer()

n, m = map(int, input().strip().split())
for _ in range(m):
    x, y, r = map(int, input().strip().split())
    edge = tuple([x, y])
    # print('edge', edge)
    w = graph[edge]
    graph[edge] = r if r < w  else w

for i in range(1, n+1):
    M.make(i)

mst_weight = 0
for edge, weight in sorted(graph.items(), key=lambda x: x[1]):
    if M.find(edge[0]) != M.find(edge[1]):
        mst_weight += weight
        M.union(edge[0], edge[1])

print(mst_weight)
