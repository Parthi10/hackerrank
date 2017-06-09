from itertools import product
from collections import defaultdict
import sys

M = 1000000007

p = set([2,3,5,7,11,13,17,19,23,29,31,37,41,43])
def good(a,b,c,d,e):
    if not a+b+c in p:
        return False
    if not b+c+d in p:
        return False
    if not c+d+e in p:
        return False
    if not a+b+c+d in p:
        return False
    if not b+c+d+e in p:
        return False
    if not a+b+c+d+e in p:
        return False
    return True

def con(a,b,c,d,e):
    return e + 10*d + 100*c + 1000*b + 10000*a

goods = defaultdict(list)
curr = defaultdict(int)
for a,b,c,d,e in product(range(10), repeat=5):
    if good(a,b,c,d,e):
        goods[con(0,a,b,c,d)].append(e)
        if a > 0:
            curr[con(a,b,c,d,e)] = 1


lim = 400001
ans = [0 for _ in range(lim + 1)]
ans[5] = len(curr.items())
ans[1] = 9
ans[2] = 90
for a,b,c in product(range(1,10), range(10), range(10)):
    if a+b+c in p:
        ans[3] += 1
for a,b,c,d in product(range(1,10), range(10), range(10), range(10)):
    if a+b+c in p and b+c+d in p and a+b+c+d in p:
        ans[4] += 1
# for i in goods:
#     print(i)
# print(ans[:7])
for n in range(6, 100):
    newcurr = defaultdict(int)
    if n == lim:
        print([i for i,v in curr.items()])
    for num, value in curr.items():
        for f in goods[num%10000]:
            k = 10*(num%10000) + f
            newcurr[k] = (newcurr[k] + value) % M
            ans[n] = (ans[n] + value) % M
    curr = newcurr

hsh, invhsh, h = defaultdict(int), defaultdict(int), 0
currl = []
for i, v in curr.items():
    currl.append(v)
    hsh[i] = h
    invhsh[h] = i
    h += 1

for n in range(100, lim + 1):
    currl = [(currl[34]+currl[56])%M,currl[48],currl[17],currl[17],currl[43],currl[55],(currl[9] + currl[31])%M,
            currl[43],currl[54],currl[7], currl[12],currl[7],currl[37],currl[54],currl[54],currl[41],currl[66],
            currl[48],currl[53],currl[66],currl[46],currl[53],currl[65],currl[65],currl[8],(currl[36]+currl[57])%M,
            currl[46],currl[65],currl[53],currl[53],currl[20],currl[47],(currl[58]+currl[60])%M,currl[20],currl[1],
            currl[1],currl[32],currl[47],currl[1],currl[1],(currl[36]+currl[57])%M,(currl[36]+currl[57])%M,(currl[22]+currl[44])%M,
            (currl[36]+currl[57])%M,currl[62],currl[4],(currl[36]+currl[57])%M,currl[50],(currl[10]+currl[25]+currl[67])%M,currl[62],
            (currl[10]+currl[25]+currl[67])%M,currl[4],currl[55],currl[50],currl[40],currl[40],currl[15],currl[6],currl[65],
            currl[15],currl[62],currl[47],currl[41],currl[30],currl[26],currl[48],currl[41],currl[42],currl[47],currl[17],currl[17]]
    ans[n] = sum(currl) % M

for _ in range(int(input())):
    sys.stdout.write(str(ans[int(input())]) + '\n')
