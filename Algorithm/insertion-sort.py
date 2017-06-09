t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split(' ')]
    count = 0
    for i in range(1,n):
        key = a[i]
        a[:i+1].sort()
        print("a", a[:i+1])
        count += abs(i-a[:i+1].index(key))
    print(count)
