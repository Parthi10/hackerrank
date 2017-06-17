a = [int(x) for x in input().strip().split(' ')]

def partition(a, first, last):
    pivot = a[last]
    wall = first-1
    for j in range(first, last):
        if a[j] < pivot:
            wall += 1
            if j!=wall: a[j],a[wall] = a[wall], a[j] #saves time. in case lik [3,2,4,1] do its partition and see
    a[wall+1],a[last] = a[last], a[wall+1]
    return wall+1

def quickSort(a, first, last):
    if first < last:
        q = partition(a, first, last)
        quickSort(a, first, q-1)
        quickSort(a, q+1, last)

quickSort(a,0,len(a)-1)
print(a)
