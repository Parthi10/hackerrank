def arrprint(arr):
	for i in arr:
		print(i, end=' ')
	print()
def insertionsort(arr):
	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]:
			while i >= 0:
				if arr[i] > arr[i+1]:
					arr[i], arr[i+1] = arr[i+1], arr[i]
				i -= 1
			arrprint(arr)
		else:
			arrprint(arr)

s = int(input())
arr = [int(x) for x in input().strip().split(' ')]

insertionsort(arr)
