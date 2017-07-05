t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    ans = ((1<<32)-1) ^ n
    print(ans)
