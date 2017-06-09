n= int(input())
a = []
firstHalf = []
for i in range(n):
    key,value = input().strip().split(' ')
    a.append([int(key), value])
    if i <= n // 2 :
        firstHalf.append(int(key))

# print(a)
for i in sorted(a):
    print(i)
    # if i[0] in firstHalf:
    #     print("-", end=" ")
    # else:
    #     print(i[1], end=" ")
    # print()
