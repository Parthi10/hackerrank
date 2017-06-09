#https://www.hackerrank.com/challenges/circular-array-rotation
n, k , q = map(int, input().split(' '))
a = [int(x) for x in input().split(' ')]
query = [int(input()) for _ in range(q)]

k = k % n
b = [0]*n
for i in range(n):
    ind = (i+k) % n
    b[ind] = a[i]

for i in query:
    print(b[i])
