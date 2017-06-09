def partition(a,first,last):
    pivot = a[last]
    wall = first-1
    for i in range(first,last):
        if a[i] < pivot:
            wall += 1
            if i != wall:
                a[i], a[wall] = a[wall], a[i]
    a[wall+1], a[last] = a[last], a[wall+1]
    print(" ".join(map(str, a)))
    return wall+1

def quicksort(a, first, last):
    if first < last:
        q = partition(a,first,last)
        quicksort(a, first, q-1)
        quicksort(a, q+1, last)

n = int(input())
a = [int(x) for x in input().strip().split(' ')]

quicksort(a, 0, n-1)
