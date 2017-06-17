def rev(s):
	r = []
	for i in range(1,len(s)+1):
		r.append(s[-i])
	return r
t = int(input())
for _ in range(t):
	s = list(input().strip())
	r = rev(s)
	flag = True
	for i in range(1,len(s)-1):
		if abs(ord(r[i]) - ord(r[i-1])) == abs(ord(s[i]) -ord(s[i-1])):
			pass
		else:
			flag = False
			break
	if flag:
		print('Funny')
	else:
		print('Not funny')