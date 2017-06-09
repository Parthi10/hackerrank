n, k = [int(x) for x in input().strip().split(' ')]
num = list(input().strip())
K = 0

l = len(num)
hl = l//2 if l%2 == 0 else (l-1)//2
lj = [] # lj = lekha-jokha, to note the indices which are changed
for i in range(hl): #let's first check how many need change
	if num[i] != num[l-1-i]:
		K += 1
if K < k:
	K = 0
	for i in range(hl):
		if num[i] != num[l-1-i]:
			if num[i] > num[l-1-i]:
				num[l-1-i] = num[i]
				lj.append(l-1-i)
				k += 1
			else:
				num[i] = num[l-1-i]
				lj.append(i)
				k += 1
elif K > k:
	print(-1)
else:
	for i in range(hl)l:
		if num[i] != num[l-1-i]:
			if num[i] > num[l-1-i]:
				num[l-1-i] = num[i]
			else:
				num[i] = num[l-1-i]
	for i in num:
		print(i, end='')
