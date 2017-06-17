g = int(input().strip())

for _ in range(g):
    n = int(input().strip())
    s = [int(x) for x in input().strip().split(' ')]
    x = 0
    for i in s:
        x ^= i
    if x:
        print("First")
    else:#x=0
        print("Second")
