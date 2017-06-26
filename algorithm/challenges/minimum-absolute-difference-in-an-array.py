n = int(input().strip())
a = [int(x) for x in input().strip().split(' ')]

a = sorted(a)
min_diff = abs(a[0] - a[1])

for i in range(1,n-1):
    diff = abs(a[i]-a[i+1])
    if min_diff>diff:
        min_diff = diff

print(min_diff)
