n, m = map(int, input().strip().split(' '))
graph = {}
for _ in range(m):
    i, j = map(int, input().strip().split(' '))
    if j in graph.keys():
        graph[j].append(i)
    else:
        graph[j] =[i]


def countChildrenEdges(graph, node):
    count = 0
    childNodes = graph[node]
    for i in childNodes:
        if i in graph.keys():
            count += countChildrenEdges(graph,i)
    count += len(childNodes)
    return count

def countchildrenNodes(graph, node):
    count = 0
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
    childNodes = graph[node]
    # print("childNodes", childNodes)
    n = len(childNodes)
    j = 0
    while j < n:
        try:
            i = childNodes[j]
            numberOfChildNodes = countchildrenNodes(graph,i)
            # print("i, numberOfChildNodes", i, numberOfChildNodes)
            if numberOfChildNodes % 2 != 0: #odd numberOfChildNodes
                graph[node].remove(i)
                removedEdges.append([node, i])
                j -= 1
                # print(graph[node])
                main(graph, i)
            j+=1
        except:
            break

main(graph, 1)
print(len(removedEdges))
