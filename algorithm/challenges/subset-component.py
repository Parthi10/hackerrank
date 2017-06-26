from itertools import combinations
from collections import defaultdict

#https://hr-testcases-us-east-1.s3.amazonaws.com/774/input03.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1498083451&Signature=LvifIaKGqmYVsBbg7zgO%2FdfXjQs%3D&response-content-type=text%2Fplain
#https://hr-testcases-us-east-1.s3.amazonaws.com/774/output03.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1498083458&Signature=jhT%2FikAatp9%2FUDq9%2BB1sZGxicZ4%3D&response-content-type=text%2Fplain
def dfs(graph, start, mark, cc):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            mark[vertex] = cc
            visited.add(vertex)
            stack.extend(x for x in graph[vertex] if x not in visited)

n = int(input().strip())
d = [int(x) for x in input().strip().split(' ')]
G = defaultdict()
for i in d:
    graph = defaultdict(list)
    b = str(bin(i)[2:])
    # print(b)
    m = len(b)
    connected_nodes = [x for x in range(m) if b[x]=='1']
    for node in connected_nodes:
        graph[node].extend(connected_nodes)
    G[i] = graph

combos = []
for i in range(1, n+1):
    combos.extend([x for x in combinations(d,i) ])

ans = 0
for num_set in combos:
    graph = defaultdict(list)
    mark = [None for x in range(64)]
    for i in num_set:
         for j in G[i]:
             graph[j].extend(G[i][j])
    cc = 1
    for i in range(64):
        if not mark[i]:
            dfs(graph, i, mark, cc)
            cc += 1
    ans += len(set(mark))
print(ans+64)
