from itertools import combinations as combo
q = int(input().strip())
for _ in range(q):
    n, m = map(int, input().strip().split(' '))
    array = [int(x) for x in input().strip().split(' ')]
    max_so_far = max_ending_here = -2**31
    c_sum = 0
    max_neg = -2**31

    for i in range(n):
        max_ending_here = max(array[i], max_ending_here + array[i])
        max_so_far = max(max_so_far, max_ending_here)

        if array[i] > 0:
            c_sum += array[i]
        else:
            if array[i] > max_neg:
                max_neg = array[i]
    if c_sum == 0: # All values were negative so just pick the largest
        c_sum = max_neg
    print(max_so_far)
    '''
    max_sum = 0
    sum_so_far = 0
    for i in range(n):
        sum_so_far = (sum_so_far + array[i]) % m
        if sum_so_far > 0:
            max_sum = max(sum_so_far, max_sum)

    print(max_sum)
    '''

    '''
    BRUTE FORCE METHOD O(n^2)
    array = list(array)
    subarrays = (sum(array[i:j]) % m for i,j in combo(range(n+1),2)])
    print(max(subarrays))
    '''
    '''
    prefix_array=[]
    curr = 0
    for i in range(n):
        curr = (array[i] % m + curr) % m
        prefix_array.append(curr)
        # prefix_array.append(sum(array[:i+1]) % m)
    '''
    '''
    #OR
    array[0] = array[0] % m
    for i in range(n):
        array[i] = (array[i - 1] %m + array[i]) % m


    ret = 0
    for i in range(n):
        for j in range(i-1,-1,-1):
            ret = max(ret, (array[i] - array[j] + m) % m)
        ret = max(ret, array[i])

    print(ret)
    '''
