n, m = map(int, input().strip().split(' '))
graph = {}
for _ in range(m):
    i, j = map(int, input().strip().split(' '))
    if j in graph.keys():
        graph[j].append(i)
    else:
        graph[j] =[i]

# def countChildrenEdges(graph, node):
#     count = 0
#     childNodes = graph[node]
#     for i in childNodes:
#         if i in graph.keys():
#             count += countChildrenEdges(graph,i)
#     count += len(childNodes)
#     return count

def countchildrenNodes(graph, node):
    count = 0
    if node not in graph.keys():
        return 0
    childNodes = graph[node]
    for i in childNodes:
        if i in graph.keys():
            count+=countchildrenNodes(graph,i)
    count += len(graph[node])

    return count

# print(graph)
global removedEdges
removedEdges = []
def main(graph, node):
    global removedEdges
    childNOdes = graph[node]
    for i in childNOdes:
        # print(i)
        numberOfChildNodes = countchildrenNodes(graph,i)
        if numberOfChildNodes % 2 != 0: #odd numberOfChildNodes
            removedEdges.append([node, i])
        if i in graph.keys(): #if not odd numberOfChildNodes still pass all of them to main() 
            main(graph, i)

main(graph, 1)
print(len(removedEdges))
