from collections import defaultdict
from itertools import combinations
import time

def get_result(binaries):
    # print("1",len(binaries))
    for i in range(64):
        indexes_with_one = []
        for ind, b in enumerate(binaries):
            if b[i] == '1':
                indexes_with_one.append(ind)
    new_list = ['0'] * 64

    for i in range(64):
        for ind in indexes_with_one:
            if binaries[ind][i] =='1':
                new_list[i] = '1'
                break
    for ind in sorted(indexes_with_one, reverse=True):
        binaries.remove(binaries[ind])
    new_list = "".join(new_list)
    binaries.append(new_list)
    # print("2",len(binaries))

    groupNodes = 0
    numberOfGroups = 0
    for b in binaries:
        g = 0
        for i in b:
            if i=='1':
                g+=1
            if g>1:
                groupNodes+= g
                numberOfGroups +=1
                break

    return (binaries, 64 - groupNodes + numberOfGroups)

n = int(input().strip())
d = [int(x) for x in input().strip().split(' ')]
t = time.time()
binaries = []
for i in d:
    graph = defaultdict(list)
    b = format(i, 'b').zfill(64)
    binaries.append(b)

combos = []
for i in range(1, n+1):
    combos.extend(list(combinations(range(n),i)))

ans = 0
mat = defaultdict(lambda:[])

for combo in combos:
    # print("checking ", combo)
    # print(mat[combo[:-1]], type(mat[combo[:-1]]), binaries[combo[-1]], type(binaries[combo[-1]]))
    b = mat[combo[:-1]]+ [binaries[combo[-1]]]
    # print(b,'\n')

    combo_bin, connectedComponents = get_result(b)
    mat[combo] = combo_bin
    ans += connectedComponents


print(64 + ans)
print(time.time()-t)
