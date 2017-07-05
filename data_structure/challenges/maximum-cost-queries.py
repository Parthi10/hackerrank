from collections import defaultdict

n, q = map(int, input().strip())
graph = defaultdict(set)
for i in range(n):
    u, v = map(int, input().strip())
    graph[u].add(v)
    graph[v].add(u)
    
for _ in range(q):
