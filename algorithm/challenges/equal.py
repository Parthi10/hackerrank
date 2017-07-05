def get_the_ans(current_list, length):
    m = min(current_list)
    min_ops = 10**9
    min_list = [x for x in range(m, m-3,-1)]#m,m-1,m-2 (these may be -ve)
    for m in min_list:
        diff_list = [x-m for x in current_list]
        number_of_ops = 0 #op=operation
        for i in diff_list:
            multiple_5 =  i // 5
            multiple_2 = (i % 5) // 2
            multiple_1 = (i % 5) % 2
            number_of_ops += multiple_5 + multiple_2 + multiple_1
        if number_of_ops<min_ops:
            min_ops = number_of_ops
    return min_ops

t = int(input().strip())
ans = []
for _ in range(t):
    n = int(input().strip())
    current_list = [int(x) for x in input().strip().split(' ')]
    ans.append(get_the_ans(current_list, n))
for i in ans:
    print(i)
