input()
num_list=set(int(x) for x in input().strip().split(' '))
def max_num(set):
    p=0
    for i in set:
        if(i>p):
            p=i
    return p
a=max_num(num_list)
num_list.remove(a)
b=max_num(num_list)
print(b)
