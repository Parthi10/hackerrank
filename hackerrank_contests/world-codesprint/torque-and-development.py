q = int(input())
for _ in range(q):
    n,m,c_lib,c_road = map(int,input().strip().split(' '))
    roads = []
    for _ in m:
        roads.append([int(x) for x in input().strip().split(' ')])
    
