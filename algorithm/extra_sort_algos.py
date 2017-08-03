def pypartition(self, start, end, array):#pythonic partition
    #less efficient than partition
    pivot = end
    i = start
    while i<pivot:
        if array[i] > array[pivot]:
            array.append(array.pop(i))
            pivot-=1
        else:
            i+=1
    return pivot

def quickSelect(array, start, end, median):#median=the index of some kth minimum
    if start == end:
        return array[median]#if start==end then start==end==median not oppos.
    pivot = partition(array, start, end)
    if pivot == median:
        return array[median]
    elif pivot<median:
        return quickSort(array, pivot+1, end, median)
    else:
        return quickSort(array, start, pivot-1, median)