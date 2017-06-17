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
