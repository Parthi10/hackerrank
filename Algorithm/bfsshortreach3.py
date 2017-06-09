from collections import defaultdict

def bfs(startingNode, endNode):
    if endNode not in graph.keys():
        return []
    queque = [[startingNode]] #to maintain a queque of paths

    while queque:
        # print(queque)
        path = queque.pop(0)
        node = path[-1]
        if node == endNode:
            return path
        for adjacent in graph[node]:
            newPath = list(path)
            newPath.append(adjacent)
            queque.append(newPath)

q = int(input().strip())
for _ in range(q):
    n, m = map(int, input().strip().split(' '))
    graph = defaultdict(list)
    for _ in range(m):
        u,v = map(int, input().strip().split(' '))
        graph[u].append(v)
        graph[v].append(u)
    startingNode = int(input().strip())
    # print(4 in graph.keys())
    for i in range(1,n+1):
        if i != startingNode:
            path = bfs(startingNode,i)
            ans = len(path)
            if ans:
                print(6*(ans-1) , end=" ")
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
