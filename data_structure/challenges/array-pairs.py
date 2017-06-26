#https://www.hackerrank.com/challenges/array-pairs
n = int(input().strip())
a = [int(x) for x in input().strip().split(' ')]

#this will take way too much memory, resulting in runtime error for large cases
mat = [[0 for x in range(n)] for y in range(n)]

for l in range(2, n+1):
    for i in range(n-l+1):
        j = i + l - 1
        if (l==2 and a[i] * a[j] <= max(a[i], a[j])):
            mat[i][j] = 1
        else:
            mat[i][j] = mat[i+1][j] + mat[i][j-1] - mat[i+1][j-1]
            if a[i] * a[j] <= max(a[i:j+1]):
                mat[i][j] += 1

print(mat[0][n-1])
