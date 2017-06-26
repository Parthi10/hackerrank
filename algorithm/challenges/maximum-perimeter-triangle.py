n = int(input().strip())
l = sorted(int(x) for x in input().strip().split())

i = n-3
while i>=0 and (l[i]+l[i+1]<=l[i+2]):
    i-=1
#now i is pointing at the index of required triplet :)
if i>=0:
    print(l[i],l[i+1],l[i+2])
else:
    print(-1)

'''
Select the longest possible side such that it can form a non-degenerate
triangle using the two sides "just smaller" than it.
It fulfills all other conditions. If no such selection is possible,
then no non-degenerate triangle exists.
'''


'''
#Brute Force Zindabad
#passes all test cases
from itertools import combinations

def area(sides):
    a,b,c = sides
    s = (a+b+c)/2
    area = s*(s-a)*(s-b)*(s-c)
    if area>0:
        return 1
    else:
        return 0

n = int(input().strip())#max 50
l = [int(x) for x in input().strip().split(' ')]
combos = set(list(combinations(l, 3)))
max_peri = 0
ans = []
for i in combos:
    peri = sum(i)
    if area(i):
        if max_peri == peri:
            ans.append(i)
        elif max_peri<peri:
            ans = [i]
            max_peri = peri

l = len(ans)
if l==0:
    print(-1)
elif l==1:
    print(" ".join(map(str, sorted(ans[0]))))
else:
    max_length_tris = []
    max_length = 0
    for i in ans:
        if max_length == max(i):
            max_length_tris.append(i)
        elif max_length<max(i):
            max_length_tris = [i]
            max_length = max(i)
    if len(max_length_tris)==1:
        print(" ".join(map(str, sorted(max_length_tris[0]))))
    else:
        min_length_tris = []
        min_length = 0
        for i in ans:
            if min_length == max(i):
                min_length_tris.append(i)
            elif min_length < min(i): #maximum shortest length
                min_length_tris = [i]
                min_length = max(i)
        if len(min_length_tris)==1:
            print(" ".join(map(str, sorted(min_length_tris[0]))))
        else:
            print(" ".join(map(str, sorted(ans[0]))))
'''
