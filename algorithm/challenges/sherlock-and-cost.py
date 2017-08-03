t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    b = [int(i) for i in input().strip().split()]
    if n==1:
        print(b[0])
        break
    s1 = 0#at any time for any i, stores the value of max S possible if a[i]=1
    s2 = 0#at any time for any i, stores the value of max S possible if a[i]=b[i]
    for i in range(1, n):
        temp = s1
        #a[i-1] for s1 was 1, and for s2 b[i-1]; same valid for i
        s1 = max(s1, s2 + abs(1 - b[i-1]))
        s2 = max(temp + abs(b[i] - 1), s2)
    print(max(s1, s2))