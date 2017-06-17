#https://www.hackerrank.com/challenges/nested-list

total=int(input())
total_list=[]
for i in range(total):
    name=input().strip()
    mark=input().strip()
    total_list.append([name,mark])
#print(total_list)

def min(total_list,total): #to find the min marks
	p=100# let it be max grade
	same_num=[0] #list to hold indices of minimum marks in total_list
	for i in range(total):
		if(float(total_list[i][1])<float(p)):
			p=total_list[i][1]
			same_num[0]=i #reserve 0th place for one of the minimums
			
	for i in range(total): #if more than one largest marks
		
		if(float(total_list[i][1])==float(p) and i!=same_num[0]):		
			same_num.append(i)
	return(same_num)
	
l=len(min(total_list, total))
for i in range(l):
	total_list.remove(total_list[same_num[i]])# remove the least marks from the total_list
#print(total_list)
same_num=min(total_list,total-l)#now get the least marks and get them printed
nameList=[]
for i in same_num:
	nameList.append(total_list[i][0])#timepass you need to do to satisfy the question, alphabetical order
#print(nameList)	
for i in sorted(nameList):# sorted cuz we have to print alphabetically
	print(i)


'''now see this:
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

'''

