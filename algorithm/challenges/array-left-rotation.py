#https://www.hackerrank.com/challenges/array-left-rotation?h_r=next-challenge&h_v=zen
n, d = map(int, input().split(' '))
array = input().split(' ')

n = len(array)
ansarray = [] #new arr because original arr once modified will disturb the rotation of other elements
for i in range(n):
    ansarray.append(array[(i+d) % n])

for i in ansarray:
    print (i, end=' ')
