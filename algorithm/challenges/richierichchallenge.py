n, k = [int(x) for x in input().strip().split(' ')]
num = list(input().strip())
K = 0
l = len(num)
hl = l//2 if l%2 == 0 else (l-1)//2
flag = True
lekh = []
for i in range(hl):
	if K < k:
		if int(num[i]) != int(num[l-1-i]):
			if num[i] > num[l-1-i]:
				num[l-1-i] = num[i]
				K += 1
				lekh.append(l-1-i)
			else:
				num[i] = num[l-1-i]
				lekh.append(i)
				K += 1
	else:
		flag = False
		break
if k > K:
	c = k-K
	i = 0
	while c > 0 and i <= hl:
		if int(num[i]) < 9 and c > 1: # c >1 because if i is changed and c dec by one
			# then c = 0 and l-1-i would not be changed and it wouldn't be a palindrom
			num[i] = 9
			if i not in lekh:
				c -= 1
			num[l-1-i] = 9
			if l-1-i not in lekh:
				c -= 1
			i +=1

		else:
			i += 1


if flag:
	for i in num:
		print(i, end='')
else:
	print(-1)
