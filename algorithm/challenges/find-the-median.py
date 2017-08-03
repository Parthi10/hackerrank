def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
def bubbleSort(array):
    alreadySorted = True
    for k in range(1, len(array)):
        for j in range(len(array)-k):
            if array[j]>array[j+1]:
                swap(array, j, j+1)
                alreadySorted = False
        if alreadySorted:
            break

    return array

def selectionSort(array):
    for k in range(len(array)-1):
        m = k
        for j in range(k+1, len(array)):
            if array[j]<array[m]:
                m = j
        if m != k:
            swap(array, k, m)
    return array
    
def insertionSort(array):
    for i in range(1, len(array)):
        hole = i
        hole_element = array[i]
        while hole>0 and array[hole-1] > hole_element:
            array[hole] = array[hole-1]
            hole -= 1
        array[hole] = hole_element
    return array
    
def partition(array, start, end):
    pivot = end
    pIndex = start
    for i in range(start, end):
        if array[i] <= array[pivot]:
            swap(array, i, pIndex)
            pIndex += 1
    swap(array, pIndex, pivot)
    return pIndex

def quickSort(array, start, end, median):
    if start == end:
        return array[median]
    pivot = partition(array, start, end)
    if pivot>median:
        return quickSort(array, start, pivot-1, median)
    elif pivot<median:
        return quickSort(array, pivot+1, end, median)
    else:
        return array[median]
    
n = int(input().strip())
a = [int(x) for x in input().strip().split()]
#a = bubbleSort(a) #only one case passes
#a = selectionSort(a) #only three cases pass
#a = insertionSort(a) #same result as selection sort
median = ((n+1)//2) - 1
ans = quickSort(a, 0, n-1, median)#passes all with swag
print(ans)
#print(a)

