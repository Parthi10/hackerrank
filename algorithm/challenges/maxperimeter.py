n = int(input())
sticks = [int(x) for x in input().strip().split()]
sumlist = []
for i in range(n-2):
    for j in range(i,n):
        for k in range(j,n):
            sumlist.append(([sticks[i],sticks[j],sticks[k]],sticks[i]+sticks[j]+sticks[k]))
p=0     
ans = []       
for i in range(len(sumlist):
	if p < sumlist[i][3]:
		p = sumlist[i][3]
		ans[0] = [sumlist[:3]]
	elif p == sumlist[i][3]:
		ans.append
		
	


#for value in trisum.
#	print(value)
