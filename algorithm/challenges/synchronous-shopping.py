n, m, k = map(int, input().strip().split(' '))
#n shopping centers, m bidirectional roads
types = []
for i in range(n):
    type_i = [int(x) for x in input().strip().split()]
    type_i.pop(0)
    types.append(type_i)
for j in range(m):
    x, y, z = map(int, input().strip().split())
