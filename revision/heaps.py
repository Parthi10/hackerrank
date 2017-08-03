class MinHeap(object):
    def __init__(self):
        self.tree = []

    def swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]

    def getParentIndex(self, childIndex):
        return childIndex//2 if childIndex & 1 else (childIndex-1)//2

    def getMin(self):
        return self.tree[0]

    def getMinChildIndex(self, parent):
        leftChild = parent*2 + 1
        rightChild = parent*2 + 2
        if rightChild<len(self.tree):
            if self.tree[leftChild]<self.tree[rightChild]:
                return leftChild
            else:
                return rightChild
        elif leftChild<len(self.tree):
            return leftChild
        return None

    def heapify(self):
        parentIndex = 0
        minChildIndex = getMinChildIndex(parentIndex)
        while minChildIndex!=None and self.tree[minChildIndex] > self.tree[parentIndex]:
            self.swap(parent, minChildIndex)
            parentIndex = minChildIndex
            minChildIndex = getMinChildIndex(parentIndex)


    def traverseUp(self, childIndex):
        parent = getParentIndex(childIndex)
        while parent >= 0 and self.tree[parent] < self.tree[childIndex]:
            self.swap(parent, childIndex)
            childIndex = parent
            parent = getParentIndex(parent)


    def insert(self, key):
        self.tree.append(key)
        self.traverseUp(len(self.tree) - 1)

    def extractMin(self):
        minKey = self.tree[0]
        self.tree[0] = self.tree[-1]
        self.tree.pop()
        self.heapify()
        return minKey

    def decrease(self, keyIndex, newValue):
        self.tree[keyIndex] = newValue
        self.traverseUp(keyIndex)

    def delete(self, keyIndex):
        self.tree[keyIndex] = float('-inf')
        self.heapify()
