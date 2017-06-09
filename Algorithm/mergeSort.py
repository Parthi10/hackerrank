#https://www.hackerrank.com/challenges/countingsort2
n = int(input())
a = [int(x) for x in input().strip().split(' ')]

#see this video : https://youtu.be/EeQ8pwjQxTM
def merge(a,b):
    size = len(a) #same as len(b)
    i = 0 #for leftList = a
    j = 0 #for rightlist = b
    mergedList = [] #sorted list of sorted subarrays
    while i < size and j < size:
        if a[i] < b[j]:
            mergedList.append(a[i])
            i += 1
        elif a[i] > b[j]:
            mergedList.append(b[j])
            j += 1
    #if still some elements in i left to be added in the mergedList
    if i < size:
        mergedList += a[i:]
    #if still some elements in b left to be added in the mergedList
    if j < size:
        mergedList += b[j:]

    return mergedList

def mergeSort(a):
    size = len(a)
    if size > 1:
        mid = size // 2
        leftList = a[:mid]
        rightList = a[mid:]
        leftList = mergeSort(leftList)
        rightList = mergeSort(rightList)

        return merge(leftList, rightList)
    else:
        return a


print(mergeSort(a))
