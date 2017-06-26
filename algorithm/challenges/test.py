from itertools import combinations
s = set([1,2,3,4])
r = set()

for pair in combinations(s, 2):
    p1, p2 = pair
    if p1 & p2:
        print(pair)
        r.add(p1 | p2)

print(r)





completed = False
while not completed:
    completed = True
    for pair in combinations(s,2):
        p1, p2 = pair
        print('got', pair)
        if p1 & p2:
            print('1', s)
            print('discarding',p1,p2)
            s.discard(p1)
            s.discard(p2)
            s.add(p1 | p2)
            print('2',s)
            completed = False
            break
print(s)
