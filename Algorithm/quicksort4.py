#https://www.hackerrank.com/challenges/quicksort4
def quicksort(a, first, last):
    quick_count = 0
    if first < last:
        pivot = a[last]
        wall = first-1
        for i in range(first,last):
            if a[i] < pivot:
                wall += 1
                a[i], a[wall] = a[wall], a[i]
                quick_count +=1
        a[wall+1], a[last] = a[last], a[wall+1]
        quick_count+=1

        q = wall+1
        quick_count += quicksort(a, first, q-1)
        quick_count += quicksort(a, q+1, last)
        return quick_count
    else:
        return 0

def insertionsort(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            while i >= 0:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    count += 1
                i -= 1
    return count

n = int(input())
a = [int(x) for x in input().strip().split(' ')]
b = a[:]
quick_count = quicksort(a, 0, n-1)
insert_count = insertionsort(b)
print(insert_count-quick_count)
