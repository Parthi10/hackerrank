q = int(input().strip())
n = int(input().strip())
for _ in range(q):
    matrix = [[0 for i in range(2*n)] for j in range(2*n)]
    for z in range(2*n):
        matrix[z] = [int(x) for x in input().strip().split(' ')]

print(matrix)
