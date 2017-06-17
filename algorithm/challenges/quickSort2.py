#https://www.hackerrank.com/challenges/quicksort2
'''
def quickSort(ar):
    if len(ar) <2 : # 0 or 1
        return(ar)
    else:
        p = ar[0]
        less = []
        more = []
        for item in ar[1:]:
            if item < p:
                less.append(item)
            else:
                more.append(item)
        l = quickSort(less)
        m = quickSort(more)
        subarray = l + [p] + m
        print(' '.join([str(x) for x in subarray]))
        return subarray


m = int(input())
ar = [int(i) for i in input().strip().split()]
quickSort(ar)

'''
def partition(a, first, last):
    if len(a)<2:
        return first
    pivot = a[first]
    wall = last+1
    for j in range(last, first,-1):
        if a[j] > pivot:
            wall -= 1
            if j!=wall: a[j],a[wall] = a[wall], a[j]
    a[wall-1],a[first] = a[first], a[wall-1]
    return wall-1

def quickSort(a, first, last):
    if first < last:
        q = partition(a, first, last)
        quickSort(a, first, q-1)
        if len(a[first:q]) > 1: print(" ".join(map(str, a[first:q])))
        quickSort(a, q+1, last)
        if len(a[q+1:last+1]) > 1: print(" ".join(map(str, a[q+1:last+1])))


a = [int(x) for x in input().strip().split(' ')]
quickSort(a,0,len(a)-1)
print(a)
