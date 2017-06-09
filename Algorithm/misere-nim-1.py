g = int(input().strip())

for _ in range(g):
    n = int(input().strip())
    s = [int(x) for x in input().strip().split(' ')]
    x = 0
    for i in s:
        x ^= i
    if len(set(s))==1 and 1 in s:
        #here x=0 or 1
        if x:#odd no. of ones
            print("Second")
        else:#even no. of ones
            print("First")
    else:
        if x:
            print("First")
        else:
            print("Second")
