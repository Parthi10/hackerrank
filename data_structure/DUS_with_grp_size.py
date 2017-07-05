from collections import defaultdict

class Node(object):

    def __init__(self, data):
        self.parent = self
        self.rank = 0
        self.data = data

class Community(object):
    def __init__(self):
        self.size = 1

class DisjoinSetsContainer(object):

    def __init__(self):
        self.map = defaultdict(lambda:None) #gives node; given data. default is set to None
        self.communityMap = defaultdict()

    def make(self, data):
        node = Node(data)
        self.map[data] = node
        new_community = Community()
        self.communityMap[node] = new_community
        return node

    def union(self, data1, data2):
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
            self.mergeCommunities(parent1, parent2)
        else:
            parent1.parent = parent2
            self.mergeCommunities(parent2, parent1)


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

    def mergeCommunities(self, newParent, oldParent):
        newCommunity = self.communityMap[newParent]
        oldCommunity = self.communityMap[oldParent]
        newCommunity.size += oldCommunity.size

M = DisjoinSetsContainer()

n, q = map(int, input().strip().split(' '))
for i in range(1, n+1):
    M.make(i)

for _ in range(q):
    inp = input().strip().split(' ')
    if inp[0]=='M':
        x, y = map(int, inp[1:])
        M.union(x, y)
    else:
        x = int(inp[1])
        parent = M.find(x)
        print(M.communityMap[parent].size)
