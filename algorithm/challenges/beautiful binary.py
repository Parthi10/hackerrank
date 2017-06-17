n=int(input().strip())
b=input().strip()
step=0
for i in range(0,n-2):
	if(b[i]+b[i+1]+b[i+2]=='010'):
		step+=1
	
print(step)
