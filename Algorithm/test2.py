d={}
tempList=[]
adjSet=set()
t=int(input())
n,m=input().split(' ')
n,m=map(int,(n,m))
for i in range(m):
	temp1,temp2=input().split(' ')
	adjSet.update(temp1,temp2)
	tempList.append([temp1, temp2])

spoint=int(input())

adjSet=list(adjSet)
for i in adjSet:
	value=[]
	for x in tempList:
		if(x[0]==i):
			value.append(x[1])
		elif(x[1]==i):
			value.append(x[0])
	d[i]=value
for i in range(1,n+1):
	if(str(i) not in d):
		d[str(i)]='None'
print(d)
