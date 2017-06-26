from collections import defaultdict
from itertools import chain, combinations
import time


def connectedCompInOneDigit(digit):
    check = digitmat[digit]
    if check:
        return check
    ret = bin(digit).count('1')
    if ret==1:
        ret = 0
    digitmat[digit] = ret
    return ret


def connectedComponents(array):
    array = tuple(set(array))
    if len(array)==0:
        return (array, 64)
    elif len(array)==1:
        return (array, min(65 - connectedCompInOneDigit(array[0]), 64))
    else:
        s = set(array)
        r = set()#stores 2, 4, 8, 16, 32..
        for i in s:
            if i!=0 and (i&(i-1)==0):
                r.add(i)
        if r:#in case of all zeros r is ()
            s -= r
        if len(s)<2:
            return connectedComponents(tuple(s))

        completed = False
        while not completed:
            completed = True
            for pair in combinations(s,2):
                p1, p2 = pair
                if p1 & p2:
                    s.discard(p1)
                    s.discard(p2)
                    s.add(p1 | p2)
                    completed = False
                    break
        ret = 0
        for i in s:
            ret += connectedCompInOneDigit(i)

        return (tuple(s), 64-ret+len(s))

n = int(input().strip())
d = [int(x) for x in input().strip().split(' ')]
t = time.time()

combos = chain.from_iterable(combinations(d, r) for r in range(n+1))
ans = 0
mat = defaultdict(lambda:())
digitmat = defaultdict(lambda:None)
for combo in combos:
    if combo:
        b = mat[combo[:-1]] + tuple([combo[-1]])
        s, r = connectedComponents(b)
        mat[combo] = s
        ans+=r

print(ans+64)
print(time.time()-t)
