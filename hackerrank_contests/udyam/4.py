from itertools import product
def fun(x):
    if x <= 9:
        return x
    sum = 0
    while(x):
        sum += x % 10
        x = x // 10
    return fun(sum)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    permo = product(list(range(1,n+1)), repeat=3)
    count = 0
    for i in permo:
        if i[0]*i[1] != i[2]:
            # print(i)
            # print(fun( fun(i[0]) * fun(i[1]) ), fun(i[2]))
            if fun( fun(i[0]) * fun(i[1]) ) == fun(i[2]):
                count += 1
    print(count)
