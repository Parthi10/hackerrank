from sys import stderr
from copy import copy
N = 64

#Handy debug function
def err(items):
    string = ""
    for item in items:
        string += str(item) + " "
    string += "\n"
    stderr.write(string)
    return

def buildSet(num):
    #Decompose num into binary and store where there are 1s
    #According to the problem statement, the set s contains
    #  the vertices of a graph that are connected to one another
    #That is, the largest connected component of the 64-node graph
    (s,i) = (set(),0)
    while num > 0:
        if num % 2:
            s.add(i)
        (num, i) = (num / 2, i + 1)

    return s

def merge(a,b):
    #Union two sets and see if there's anything in common
    union = copy(a)
    overlap = False
    for elem in b:
        if elem in a:
            overlap = True
        else:
            union.add(elem)
    return (union, overlap)

def solve(sets, start, n, prev, prevContrib):
    #Recursive function that tests every combo of numbers/components
    ans = 0
    for i in range(start, n):
        component = sets[i]
        #If the size of the largest component is bigger than 1...
        if len(component) > 1:
            #Upon incorporating the component, the bits change
            (newBits, overlap) = merge(prev, component)
            #If just starting or there's overlap between prev. and current component
            #  there's just one component larger than 1
            if len(prev) == 0 or overlap:
                contrib = N - len(newBits) + 1
            #Otherwise, there are two
            else:
                contrib = prevContrib + 1 - len(component)
        #Otherwise, this number contributes no new edges
        else:
            (newBits, contrib) = (prev, prevContrib)
        ans += contrib + solve(sets, i+1, n, newBits, contrib)
        
    return ans

if __name__ == "__main__":
    n = int(raw_input().strip())
    sets = []
    for num in map(int,raw_input().strip().split()):
        s = buildSet(num)
        sets.append(s)

    print N + solve(sets, 0, n, set(), 64)

'''
def solve(d):
    result = 64
    n = len(d)
    dp = [[] for i in xrange(2**n)]
    for i in xrange(n):
        o = 2 ** i
        e = d[i]
        ebit = bin(e).count("1")
        for j in xrange (o):
            subset = dp[j]
            if not subset:
                if ebit > 1:
                    cc = [e]
                else:
                    cc = []
            else:
                if ebit > 1:
                    no_merge = True
                    cc = dp[j]
                    cc = cc[:]
                    for i, a in enumerate(cc):
                        if a & e:
                            # connected
                            cc[i] = a | e
                            no_merge = False
                    if no_merge:
                        cc.append(e)
                else:
                    cc = dp[j]
            #len_cc = filter(lambda x: x > 1, map(lambda x: bin(x).count("1"), cc))
            len_cc = map(lambda x: bin(x).count("1"), cc)
            result += 64 - sum(len_cc) + len(len_cc)
            dp[o + j] = cc

    return result

def test():
    n = input()
    d = raw_input()
    d = map(int, d.strip().split())
    print solve(d)

test()
'''
'''
#!/usr/bin/env python
from itertools import chain, combinations
import time
def powerset(S):
  s = list(S)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def bitset(v):
  s = set()
  for i in xrange(64):
    if v & (1<<i):
      s.add(i)
  if len(s) == 1:
    s = set()
  return s

def count_components(s):
  if len(s) == 0:
    return 64
  elif len(s) == 1:
    return min(65 - len(bitset(s[0])), 64)

  s = set(s)
  r = set()
  for i in s:
    if i != 0 and ((i & (i-1)) == 0):
      r.add(i)
  s -= r

  if len(s) < 2:
    return count_components(tuple(s))

  complete = False
  while not complete:
    complete = True
    for p in combinations(s, 2):
      if p[0] & p[1] != 0:
        s.discard(p[0])
        s.discard(p[1])
        s.add(p[0] | p[1])
        complete = False
        break

  return 64 - sum(len(bitset(x)) for x in s) + len(s)

if __name__ == "__main__":
  n = int(raw_input())
  v = map(int, raw_input().split())
  t = time.time()

  print sum(count_components(s) for s in powerset(v))
  print time.time() - t
'''
'''
def find(l, i):
    if l[i]!=i:
        l[i] = find(l, l[i])
    return l[i]

def go():
    n = input()
    d = map(int, raw_input().split())
    l = range(n)
    for i in range(n):
        for j in range(i):#j>i
            if d[i]&d[j]:
                fi = find(l, i)
                fj = find(l, j)
                l[fi] = l[fj]#fi > fj
    #l has smallest number as the representative of the groups/sets of connected_nodes
    print 'l', l

    q = [[] for i in range(n)]

    for i in range(n):
        q[find(l,i)].append(d[i])
    print(q)
    res = 64<<n
    for i in range(n):
        if q[i]:
            lq = len(q[i])
            v = (64<<lq) - f(lq, q[i])
            res -= (1<<(n - lq)) * v
    print res

def f(n, d):
    res = 64
    dp = [0]*(1<<n)
    print("len(dp)", len(dp))
    dp[0] = [1<<i for i in range(64)]
    for i in range(1, 1<<n):#1,..2**n
        for j in range(n):
            if i & (1<<j):#2**j == i
                break

        v = d[j]
        q = dp[i & (i-1)]
        if v:
            l = []
            for x in q:
                if x & v:
                    v|=x
                else:
                    l.append(x)
            l.append(v)
            res += len(l)
            dp[i] = l
        else:
            res += len(q)
            dp[i] = q
    return res

go()
'''
