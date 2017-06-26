from itertools import combinations
from collections import defaultdict

class Node(object):

    def __init__(self, data):
        self.parent = self
        self.rank = 0
        self.data = data

class DisjoinSetsContainer(object):

    def __init__(self):
        self.map = defaultdict(lambda:None) #gives node; given data. default is set to None
        self.size = 0

    def make(self, data):
        node = Node(data)
        self.map[data] = node
        self.size += 1
        return node

    def reset(self):
        for node in self.map.values():
            node.parent = node
            node.rank = 0
        self.size = 64

    def union(self, data1, data2):
        # print("got", data1, data2, self.disjointSetList)
        node1 = self.map[data1]
        node2 = self.map[data2]

        if not node1:
            node1 = self.make(data1)
        if not node2:
            node2 = self.make(data2)

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
        self.size -= 1

    def get_size(self):
        return self.size

    def find(self, data): #there's a set with data: data
        node = self.map[data]
        node_parent = node.parent
        if node_parent.parent == node_parent:
            return node_parent


        #path compression, iteratively
        nodes_in_between = []
        while node != node.parent:
            nodes_in_between.append(node)
            node = node.parent

        if nodes_in_between:
            for i in nodes_in_between:
                i.parent = node
        return node


n = int(input().strip())
d = [int(x) for x in input().strip().split(' ')]
#https://github.com/kfstorm/HackerRank/tree/master/cases/subset-component


G = defaultdict(list)
for i in d:
    graph = defaultdict(list)
    b = format(i, 'b').zfill(64)
    print(b)
    for j in range(len(b)):
        if b[j]=='1':
            G[i].append(j)
    print(b)

combos = []
for i in range(1, n+1):
    combos.extend([x for x in combinations(d,i) ])

D = DisjoinSetsContainer()
for i in range(64):
    D.make(i)

ans = 0
for num_set in combos:
    for num in num_set:
        connected_nodes = G[num]
        for i in range(len(connected_nodes)-1):
            D.union(connected_nodes[i], connected_nodes[i+1])
    ans+= D.get_size()
    D.reset()

print(ans+64)
