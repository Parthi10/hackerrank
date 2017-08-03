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

class Graph(object):
    def __init__(self, vertices):#n=total no. of nodes
        self.weightMatrix = [[0 for x in range(len(vertices))] for y in range(len(vertices))]
        self.adjList = defaultdict(set)
        self.vertices = defaultdict(lambda:None)#vertex = index
        for index, vertex in enumerate(vertices):
            self.vertices[vertex] = index

    def addEdge(self, u, v, w):
        self.adjList[u].add(v)
        self.adjList[v].add(u)
        u, v = self.vertices[u], self.vertices[v]
        w_ = self.weightMatrix[u][v]
        if w_==0 or w_ > w:#in case of multiple weights add only smaller one
            self.weightMatrix[u][v] = \
                self.weightMatrix[v][u] = w

    def getWeight(self, u, v):
        u = self.vertices[u]
        v = self.vertices[v]
        return self.weightMatrix[u][v]

#list of all vertices
vertices = ['D', 'B', 'F', 'A', 'E', 'C']

#construct graph
graph = Graph(vertices)

graph.addEdge('A', 'B', 3);
graph.addEdge('B', 'C', 1);
graph.addEdge('C', 'A', 1);
graph.addEdge('A', 'D', 1);
graph.addEdge('B', 'D', 3);
graph.addEdge('D', 'E', 6);
graph.addEdge('E', 'F', 2);
graph.addEdge('C', 'E', 5);
graph.addEdge('C', 'F', 4);

#map of vertex to edge which gave minimum weight to this vertex
vertexToEdge = defaultdict(lambda:None)

#store the result
result = []

#Bin Min heap data structure
BinMin = BinMinHeap_Map()

#insert all vertices with inf weight initially
for vertex in vertices:
    BinMin.insert(float('inf'), vertex)

startVertex = 'A'
BinMin.decreaseKey(startVertex,  0)

while(BinMin.notEmpty()):
    minKey = BinMin.extractMin()
    spanningTreeEdge = vertexToEdge[minKey]
    if spanningTreeEdge:
        result.append(spanningTreeEdge)

    for adjVertex in graph.adjList[minKey]:
        # print("\n\nchecking",minKey, adjVertex)
        # BinMin.seeHeap()
        if BinMin.containsKey(adjVertex):
            # print("inside contains")
            edgeWeight = graph.getWeight(minKey, adjVertex)
            weightInheap = BinMin.weightOfKey(adjVertex)
            # print(edgeWeight, weightInheap)
            if edgeWeight < weightInheap:
                BinMin.decreaseKey(adjVertex, edgeWeight)
                vertexToEdge[adjVertex] = [minKey, adjVertex]
                # print(BinMin.heap[BinMin.map[adjVertex]].weight)
        # BinMin.seeHeap()


    # print(dict(vertexToEdge))
print(result)
