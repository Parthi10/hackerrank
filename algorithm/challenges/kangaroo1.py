x1,v1,x2,v2 = map(int, input().strip().split(' '))
print("YES" if v1 > v2 and (x2 - x1) % (v2 - v1) == 0 else "NO")
