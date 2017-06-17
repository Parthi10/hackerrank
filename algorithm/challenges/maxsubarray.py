def kadanes(a,n): #subarray (contigous)
    #if all values -ve; kadanes not gonna work
    #in that case the least -ve to be returned, all_negatives flag to check that
    summ = 0
    ans = 0
    all_negatives = True
    for i in range(n):
        if summ + a[i] > 0:
            summ += a[i]
            if all_negatives:
                all_negatives = False
            ans = max(summ, ans)
        else:
             summ = 0
    return max(a) if all_negatives else ans


def get_max_non_contigous_subarray_sum(a, n):
    if any(i>0 for i in a): #true if atlest one +ve in array
        return sum([x for x in a if x>0])
    else:
        return max(a)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    array = [int(x) for x in input().strip().split(' ')]
    max_contigous_subarray_sum = kadanes(array, n)
    max_non_contigous_subarray_sum = get_max_non_contigous_subarray_sum(array, n)
    print(max_contigous_subarray_sum, max_non_contigous_subarray_sum)
