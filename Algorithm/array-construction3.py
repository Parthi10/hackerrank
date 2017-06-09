from itertools import combinations, combinations_with_replacement

intlist = [0,1,2,3,4,5,6,7,8,9]
q = int(input().strip())

def get_abs_diff_sum(array,k):
    abs_diff_sum = 0
    for i in range(n):
        for j in range(i,n):
            abs_diff_sum += abs(array[i]-array[j])
            if abs_diff_sum>k:
                break

    return abs_diff_sum

def get_sum(array,s):
    array_sum=0
    for i in array:
        array_sum += i
        if array_sum >s:
            break

    return array_sum

def get_array_of_given_sum(no_of_digits, given_sum):
    print("got", no_of_digits, given_sum)
    if no_of_digits==0:
        return [0]

    array_list = []

    for i in range(10):
        if given_sum-i>0:
            print("recursive call")
            array_list.append(get_array_of_given_sum(no_of_digits-1, given_sum-i))
    print("returning", array_list)
    return array_list


for _ in range(q):
    n,s,k = map(int, input().strip().split(' '))
    print(get_array_of_given_sum(n, s))

    # flag=True

    # for array in combinations_with_replacement(intlist,n):
        # print()
        # array_sum = get_sum(array,s)
    #     if array_sum == s:
    #         abs_diff_sum = get_abs_diff_sum(array,k)
    #         if abs_diff_sum == k:
    #             print(" ".join(map(str, array)))
    #             flag=False
    #             break
    # if flag:
    #     print("-1")
