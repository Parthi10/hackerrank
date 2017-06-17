#https://www.hackerrank.com/challenges/quicksort1
def partition(a, first, last):
    pivot = a[first]
    wall = last+1
    for j in range(last, first,-1):
        if a[j] > pivot:
            wall -= 1
            if j!=wall: a[j],a[wall] = a[wall], a[j] #saves time. in case lik [3,2,4,1] do its partition and see
    a[wall-1],a[first] = a[first], a[wall-1]
    return a

n = int(input())
a = [int(x) for x in input().strip().split(' ')]
partition(a,0,n-1)
print(" ".join(map(str,a)))
