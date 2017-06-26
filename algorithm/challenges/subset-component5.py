from collections import defaultdict
from itertools import chain, combinations
import time

def get_result(array):
    s = set(array)
    # print('in array',array)
    for pair in combinations(array,2):
        p1, p2 = pair
        # print('p12',p1,p2)
        if p1 & p2:
            s.discard(p1)
            s.discard(p2)
            s.add(p1 | p2)

    ret = 0
    # print("s",s)
    for i in s:
        ret += connectedCompInOneDigit(i)

    return (list(s), min(65-ret, 64))


def connectedCompInOneDigit(digit):
    ret = 0
    for i in range(64):
        if digit & 1<<i:
            ret += 1
    if ret==1:
        return 0
    return ret

def connectedComponents(combos):
    mat = defaultdict(lambda:[])
    ans = 0
    for combo in combos:
        if combo==():
            ans+=64
        elif len(combo)==1:
            mat[combo]=list(combo)
            # print(combo)
            # print(connectedCompInOneDigit(combo[0]))
            ans+=min(65 - connectedCompInOneDigit(combo[0]), 64)
        else:
            # print('combo',combo, mat[combo[:-1]], combo[-1])
            b = mat[combo[:-1]] + [combo[-1]]
            # print('b',b)
            combo_bin, connectedComponents = get_result(b)
            mat[combo] = combo_bin
            ans += connectedComponents
            # print(connectedComponents)
    return ans
n = int(input().strip())
d = [int(x) for x in input().strip().split(' ')]
t = time.time()

combos = chain.from_iterable(combinations(d, r) for r in range(n+1))
ans = connectedComponents(combos)
print(ans)
print(time.time()-t)
