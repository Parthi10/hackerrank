#!/bin/python3

import sys
from collections import defaultdict


def two_pal(a,b, k_list):
    if a==b:
        return True
    if b in k_list[a] or a in k_list[b]:
        return True
    return False

def longest_pal(a, m, k_list):
    mat = [[0 for x in range(m)] for y in range(m)]
    for x in range(m):
        mat[x][x] = 1

    for l in range(2, m+1):
        for i in range(m-l+1):
            j = i + l - 1
            if l==2 and two_pal(a[i], a[j], k_list):
                mat[i][j] = 2
            elif two_pal(a[i],a[j], k_list):
                mat[i][j] = 2 + mat[i+1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i+1][j])

    return mat[0][m-1]

def graph_components(edges):
    components = []
    for v1, v2 in edges:
        for component in components:
            if v1 in component or v2 in component:
                component.add(v1)
                component.add(v2)
                break
        else:
            components.append({v1, v2})

    # components = [list(component) for component in components]
    return components



k_list = []
n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
element_list = set()
for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    element_list.add(x)
    element_list.add(y)
    k_list.append(sorted([x,y]))

print(k_list)
print(sorted(k_list))
k_list = graph_components(k_list)

print(k_list)

k_dict = defaultdict(list)

for l in k_list:
    for i in l:
        k_dict[i] = l


a = list(map(int, input().strip().split(' ')))
print(k_dict)
print(longest_pal(a, m, k_dict))
