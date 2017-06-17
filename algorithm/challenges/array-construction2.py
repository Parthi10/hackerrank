from itertools import combinations, combinations_with_replacement

intlist = [0,1,2,3,4,5,6,7,8,9]
q = int(input().strip())

def get_abs_diff_sum(array,k):
    abs_diff_sum = 0
    for i in range(n):
        for j in range(i,n):
            abs_diff_sum += abs(array[i]-array[j])
            if abs_diff_sum>k:
                break

    return abs_diff_sum

def get_sum(array,s):
    array_sum=0
    for i in array:
        array_sum += i
        if array_sum >s:
            break

    return array_sum

for _ in range(q):
    n,s,k = map(int, input().strip().split(' '))
    flag=True
    for array in combinations_with_replacement(intlist,n):
        array_sum = get_sum(array,s)
        if array_sum == s:
            abs_diff_sum = get_abs_diff_sum(array,k)
            if abs_diff_sum == k:
                print(" ".join(map(str, array)))
                flag=False
                break
    if flag:
        print("-1")
