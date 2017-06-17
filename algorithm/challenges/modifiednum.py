def check(n):

	sqlist = str(n**2)# list(map(int,str(n**2)))
	l = len(sqlist)
	if l%2 == 0: #if even
		rsq = int(sqlist[l//2:])
		lsq = int(sqlist[:l//2]) 
	else:
		rsq = int(sqlist[(l-1)//2:])
		if l!= 1:
			lsq = int(sqlist[:(l-1)//2])
		else:
			lsq = 0 #only lsq can have an empty list
	if rsq + lsq == n:  
		return True

p = int(input())
q = int(input())
ans = []
for i in range(p, q+1):
	if check(i) == True:
		ans.append(i)
if len(ans)!= 0:
	for i in ans:
		print(i, end =' ')
else:
	print('INVALID RANGE')

#for i in [1,9,45,55,99]:
	#print(check(i))
