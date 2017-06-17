from collections import defaultdict
'''
MY OWN CODE
PASSES 3/6 TEST CASES, REST TIME OUT.
'''
def find_shortest_path(graph,startNode, endNode, path=[]):
    if endNode in path:
        return None
    if startNode not in graph:
        return None
    path.append(startNode)
    if startNode == endNode:
        return path

    nextNodes = graph[startNode]
    shortest = None
    for node in nextNodes:
        if node not in path:
            newPath = find_shortest_path(graph,node, endNode, path[:])
            if newPath:
                if not shortest or len(newPath) < len(shortest):
                    shortest = newPath
    return shortest

q = int(input().strip())
for _ in range(q):
    n, m = map(int, input().strip().split(' '))
    graph = defaultdict(list)
    for _ in range(m):
        u,v = map(int, input().strip().split(' '))
        graph[u].append(v)
        graph[v].append(u)
    startingNode = int(input().strip())

    for i in range(1,n+1):
        if i != startingNode:
            path = find_shortest_path(graph,startingNode,i,[])
            if path:
                print(6*(len(path)-1), end=" ")
            else:
                print("-1", end=" ")
    print()



'''

1
7 6
1 2
1 3
1 7
7 6
3 4
4 5
3

'''
