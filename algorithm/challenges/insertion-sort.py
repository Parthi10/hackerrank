#Regular insertionsort and iteratively counting number of
#shifts are not gonna work in this question.

def merge_sort(array):
    shifts = 0
    if len(array)==1:
        return shifts
    L = array[:len(array)//2]
    R = array[len(array)//2:]
    shifts += merge_sort(L)
    shifts += merge_sort(R)

    nL, nR = len(L), len(R)
    l, r, i = 0, 0, 0

    while l<nL and r<nR:
        if L[l] <= R[r]:
            array[i] = L[l]; l += 1
        else:
            array[i] = R[r]; r += 1
            shifts += nL - l
        i+=1

    while l<nL:
        array[i] = L[l]
        l+=1; i+=1

    while r<nR:
        array[i] = R[r]
        r+=1; i+=1

    return shifts

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    array = [int(x) for x in input().strip().split(' ')]
    print(merge_sort(array))
