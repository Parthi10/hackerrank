n = int(input().strip())
s = list(input().strip())
k = int(input().strip())
k=k if k<26 else k%26 #this is awesomely hidden, analyse it
for i in range(len(s)):
	a=ord(s[i])
	na=a+k
	if((a>=97 and a<=122) or (a>=65 and a<=90) ): #should be alphabet
		if((a>=97 and a<=122)):#if capital
			if(na>122 ):
				na=na-26
		elif((a>=65 and a<=90)):# if small
			if(na>90):
				na=na-26
		s.pop(i)# remove it
		s.insert(i, chr(na))# insert the desired char at the removed char's space

for i in s:
	print(i, end='')

print()
