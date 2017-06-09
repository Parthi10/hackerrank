from itertools import combinations, combinations_with_replacement

intlist = [0,1,2,3,4,5,6,7,8,9]
q = int(input().strip())


for _ in range(q):
    n,s,k = map(int, input().strip().split(' '))
    for array in combinations_with_replacement(intlist,n):
        print(array)
        if sum(array) == s:
            if sum([abs(i[0]-i[1]) for i in combinations(array, 2) ]) == k:
                print(" ".join(map(str, array)))
                break
