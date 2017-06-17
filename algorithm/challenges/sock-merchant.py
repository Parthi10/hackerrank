n = int(input().strip())
c = [int(x) for x in input().strip().split(' ')]
count_ = []
socks = list(set(c))
for j in socks:
    count_.append(c.count(j))

ans = 0
for k in count_:
    ans += k//2
    
print(ans)
