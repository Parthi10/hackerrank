#https://www.hackerrank.com/challenges/equal

def get_the_ans(current_list, length):
    m = min(current_list)
    all_op_list = []#list of number of ops for m = m to m-3 targets
    min_list = [x for x in range(m,m-3,-1) if x>=0]
    for m in min_list:
        target_list = [m]*length
        diff_list = [x-y for x,y in zip(current_list, target_list)]
        number_of_ops = 0 #op=operation
        for i in diff_list:
            multiple_5 =  i // 5
            multiple_2 = (i % 5) // 2
            multiple_1 = (i % 5) % 2
            number_of_ops += multiple_5 + multiple_2 + multiple_1
        all_op_list.append(number_of_ops)
    return min(all_op_list)


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    current_list = [int(x) for x in input().strip().split(' ')]
    print(get_the_ans(current_list, n))
