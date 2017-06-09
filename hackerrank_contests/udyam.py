n = int(input().strip())
ids = [int(x) for x in input().strip().split(' ')]

ans_list = []

def get_contiguous(array, index):
    n = len(array[index:])
    i = index+1
    M = array[index]
    contiguous_number = 1
    flag = True
    unique = 0
    while True:
        try:
            if array[i] != M and flag:
                flag = False
                unique = array[i] #first unique num set
                i += 1
            if array[i] == M or array[i] == unique:
                if array[i] == M:
                    contiguous_number+=1
                i+=1
            else:
                #new number spotted
                return contiguous_number
        except:
            return contiguous_number

for i in range(n):
    ans_list.append(get_contiguous(ids, i))
print(max(ans_list))
# array = [2,7,3,7,7,3,7,5,7]
# index = 1
# print(get_contiguous(array, index))
