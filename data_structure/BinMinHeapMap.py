from collections import defaultdict

class Node(object):#used in BinMinHeap_Map
    def __init__(self, weight=None, key=None):
        self.weight = weight
        self.key = key

#DS to store [key, weight] in Bin min heap and have a map of key with weight
class BinMinHeap_Map(object):

    def __init__(self):
        self.heap = []#to contain nodes
        self.map = defaultdict(lambda:None)#contains indexes of vertices in self.heap list

    def seeHeap(self):
        for i in self.heap:
            print(i.key, i.weight, end=" ")
        print()

    def parent(self, index):
        return (index-1)//2 if index!=0 else 0

    def containsKey(self, key):
        return True if self.map[key] != None else False

    def weightOfKey(self, key):
        if self.containsKey(key):
            return self.heap[self.map[key]].weight

    def swap(self, index, parentIndex):
        self.heap[index], self.heap[parentIndex] = \
            self.heap[parentIndex], self.heap[index]

    def updateMap(self, node, parentNode):
        self.map[node.key], self.map[parentNode.key] = \
            self.map[parentNode.key], self.map[node.key]

    def fixTheHeap(self, index):#bubble up
        parentIndex = (index - 1) // 2
        while (parentIndex>=0):
            parentNode = self.heap[parentIndex]
            node = self.heap[index]
            if node.weight < parentNode.weight:
                self.swap(index, parentIndex)
                self.updateMap(node, parentNode)
                index = parentIndex
                parentIndex = self.parent(index)
            else:
                break

    def insert(self, weight, key):#pair = [key, weight]
        node = Node(weight=weight, key=key)
        self.heap.append(node)
        index = len(self.heap) - 1
        self.map[key] = index
        self.fixTheHeap(index)

    def decreaseKey(self, key, new_val):
        index = self.map[key]
        self.heap[index].weight = new_val
        self.fixTheHeap(index)

    #https://en.wikipedia.org/wiki/Binary_heap#Extract
    def heapify(self, index=0):
        lastIndex = len(self.heap) - 1
        left = index * 2 + 1
        right = index * 2 + 2
        smallestIndex = smallerIndex = index#smallestIndex in sense of index with smallest weight among child
        if right <= lastIndex:#right and left both index present in self.heap list
            smallerIndex = left if (self.heap[left].weight < self.heap[right].weight) else right
        elif left <= lastIndex:
            smallerIndex = left

        if smallerIndex!=index and self.heap[smallerIndex].weight < self.heap[index].weight:
            smallestIndex = smallerIndex

        if smallestIndex != index:
            self.swap(index, smallestIndex)
            self.updateMap(self.heap[smallestIndex], self.heap[index])
            self.heapify(index=smallerIndex)

    def extractMin(self):
        minNode = self.heap.pop(0)#O(1)
        if self.notEmpty():
            self.heap.insert(0, self.heap.pop())#O(1) as index is 0
            del self.map[minNode.key]
            self.map[self.getMin()] = 0
            self.heapify()
        return minNode.key

    def getMin(self):
        return self.heap[0].key

    def notEmpty(self):
        return bool(len(self.heap))

