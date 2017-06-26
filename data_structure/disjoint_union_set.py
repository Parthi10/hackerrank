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


M = DisjoinSetsContainer()

n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
for a0 in range(k):
    x,y = input().strip().split(' ') #data1 data2
    x,y = [int(x),int(y)]
    M.union(x, y)

a = list(map(int, input().strip().split(' ')))
for i in a:
    print(i, M.find(i).data)
