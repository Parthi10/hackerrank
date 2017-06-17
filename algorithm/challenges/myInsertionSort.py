a = [int(x) for x in input().strip().split(' ')]
'''
for i in range(1,len(a)):
    j=i-1
    key = a[i]
    while j>=0 and a[j]>key:
        a[j], a[j+1] = key, a[j]
        j -= 1
'''
#   OR
for i in range(1,len(a)):
    j=i-1
    key = a[i]
    while j>=0 and a[j]>key:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key

print(a)
