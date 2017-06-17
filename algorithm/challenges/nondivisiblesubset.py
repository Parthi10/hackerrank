n,k = [int(x) for x in input().strip().split(' ')]

a = [int(x) for x in input().strip().split(' ')]

subset = []
for i in range(len(a)):# make a list of all the elements whose sum with i is not evenly divisible
	s = []
	for j in range(len(a)):
		if (a[i]+a[j]) % k != 0 and i != j:
			s.append(a[j])
	subset.append([a[i],s])
ans = 0

for i in range(len(subset)):
	if ans < len(subset[i][1]):
		ans = len(subset[i][1])


print(1+ans)
