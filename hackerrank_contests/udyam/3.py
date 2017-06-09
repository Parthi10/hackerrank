n = int(input().strip())
l = []
for i in range(n):
    #l.append(input().strip())
    l.append([int(x) for x in input().strip().split(' ')])
print(" ".join(map(str, l[0])))
