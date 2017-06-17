q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    c = map(int, input().strip().split(' '))
    edges = []
    for j in range(n-1):
        edges.append(list(map(int, input().strip().split(' '))))
        
