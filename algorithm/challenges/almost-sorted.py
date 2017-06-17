n = int(input().strip())
array = [int(x) for x in input().strip().split(' ')]

sorted_array = sorted(array)

i = 0

while i<n:
    if array[i] > array[i+1]:
        array[i+1], array[i] = array[i], array[i+1]
        if array == sorted_array:
            print("swap ", i+1, i+2)
            break
