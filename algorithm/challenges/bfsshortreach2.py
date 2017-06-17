from collections import defaultdict

def bfs(startingNode):
    visited = [False]*(n+1)
    queque = []
    visited[startingNode] = True
    queque.append(startingNode)
    traversed_path = [startingNode]

    while queque:
        s = queque.pop(0)
        for i in graph[s]:
            if visited[i] is False:
                queque.append(i)
                visited[i] = True
                traversed_path.append(i)

    return traversed_path

def bfs_all(startingNode):
    queque = [[startingNode]] #to maintain a queque of paths
    traversed_path = queque[:]
    while queque:
        # print(queque)
        path = queque.pop(0)
        node = path[-1]
        if graph[node]:
            for adjacent in graph[node]:
                newPath = list(path)
                newPath.append(adjacent)
                queque.append(newPath)
                traversed_path.append(newPath)
        else:
            break
    return traversed_path

q = int(input().strip())
for _ in range(q):
    n, m = map(int, input().strip().split(' '))
    graph = defaultdict(list)
    for _ in range(m):
        u,v = map(int, input().strip().split(' '))
        graph[u].append(v)
        graph[v].append(u)
    startingNode = int(input().strip())
    traversed_path = bfs_all(startingNode)
    print(traversed_path)
    # for i in range(1,n+1):
    #     if i != startingNode:
    #         if i in nodeList:
    #             path_count = bfs(i)
    #             print(6*(path_count-1), end=" ")
    #         else:
    #             print("-1", end=" ")
    print()
