#!/bin/python3

# import sys
# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
# b = [int(b_temp) for b_temp in input().strip().split(' ')]
# ans=[]
# for i in b:
#     for j in a:
#         ans.append(i//j)
# ans1 = []
# flag = 1
# for x in ans:
#     for i in b:
#         for j in a:
#             if i%x != 0 or x%j != 0:
#                 flag = 0
#                 break
#     if flag:
#         print(x)
#         ans1.append(x)
# print(len(ans1))
#!/bin/python3

import sys

def getTotalX(a, b):
    largest_of_a = max(a)
    smallest_of_b = min(b)
    focus_list = [x for x in range(largest_of_a, smallest_of_b+1, largest_of_a)]
    focus_list_copy = focus_list[:]
    for i in focus_list_copy:
        for j in b:
            if j % i != 0:
                focus_list.remove(i)
                break

    focus_list_copy = focus_list[:]
    for i in focus_list_copy:
        for j in a:
            if i % j !=0:
                focus_list.remove(i)
                break
    return len(focus_list)

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)

'''
Find the LCM of a, then set range of focus_list as range(LCM, smallest_of_b+1, LCM)
no need to check i % ai in another loop 
'''
