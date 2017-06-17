from itertools import product
k, m = map(int, input().strip().split(' '))
lists = [map(int, input().strip().split(' ')[1:]) for _ in range(k)]

def f(*x):
    # print(x)
    return sum(i**2 for i in x[0])%m

a = map(f, product(*lists))
print(max(a))
# a = product(*lists)
# for i in a:
#     print(i)
