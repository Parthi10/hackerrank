def arrprint(arr):
	for i in arr:
		print(i, end=' ')
	print()
def InsertionSort(arr, e):
	for i in range(len(arr)-2,-1,-1):
		if arr[i] > e:
			arr[i+1] = arr[i]
			arrprint(arr)
		elif arr[i] < e:
			arr[i+1] = e
			arrprint(arr)
			break
	if e not in arr:
		arr[0] = e
		arrprint(arr)

size = int(input())
arr = [int(x) for x in input().strip().split(' ')]
InsertionSort(arr, arr[size-1])
