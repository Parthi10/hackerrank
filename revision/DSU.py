class Node(object):
    def __init__(self, data=None):
        self.parent = self
        self.data = data
        self.rank = 0


class DSU(object):
    def __init__(self):
        self.map = defaultdict(lambda:None)

    def make(self, data):
        self.map[data] = Node(data=data)
        return self.map[data]

    def union(self, data1, data2):
        node1 = self.map[data1]
        if not node1:
            node1 = self.make(data1)

        node2 = self.map[data2]
        if not node2:
            node2 = self.make(data2)

        parent1 = self.find(data1)
        parent2 = self.find(data2)

        if parent1 == parent2:
            return

        elif parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2

    def find(self, data):
        node = self.map[data]
        if node.parent.parent != node.parent:
            node.parent = self.find(node.parent.data)
        return node.parent
