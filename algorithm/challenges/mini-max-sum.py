#https://www.hackerrank.com/challenges/mini-max-sum
from itertools import combinations
a = [int(x) for x in input().strip().split(' ')]

combo = list(combinations(a,4))
ans = []
for i in combo:
    ans.append(sum(i))
print(min(ans),max(ans))
