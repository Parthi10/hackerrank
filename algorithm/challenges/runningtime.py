#https://www.hackerrank.com/challenges/runningtime
n = int(input())
a = [int(x) for x in input().strip().split(' ')]

def insertionSort(a):
    shift = 0
    for i in range(1,len(a)):
        j = i-1
        key = a[j+1]
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            shift += 1
            j -= 1
        a[j+1] = key
    return shift

print(count)
