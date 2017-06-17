n,m = map(int, input().strip().split(' '))#n is no. of people
topchart=[]#chart of topics who knows who don't
for i in range(n):
	temp = list(input().strip())
	topchart.append(temp)
max_topic=0

for i in range(n):# i is each person
	for j in range(i+1,n):# j's are other persons who can team-up with i
		temp=topchart[i][:]
		for index,k in enumerate(topchart[j]):
			if k == '1' and temp[index]!='1':
				temp[index]='1'
		#for loop ke bahar aane par i has got his team topic chart, i.e. temp.
		max_topic_temp=temp.count('1')
		if max_topic<max_topic_temp:
			max_topic = max_topic_temp
			max_teams=1
		elif max_topic == max_topic_temp:
			max_teams+=1

print(max_topic)
print(max_teams)
'''
import itertools
N,M = map(int,input().strip().split())
knowledge=[]
for i in range(N):
    knowledge.append(int(input(),2))# appending after converting bin into dec
mx = -float('inf')# negative infinity
teams=0
for p1,p2 in itertools.combinations(range(N),2):
    combined_topics = bin(knowledge[p1]|knowledge[p2]).count('1')
    if (combined_topics==mx):
        teams+=1
    elif (combined_topics>mx):
        mx = combined_topics
        teams=1

print(mx,teams,sep='\n')
'''










#import operator
#def onesearch(a):# return the no. of 1's  in list a
	#p=0
	#for i in a:
		#if i == '1':
			#p+=1
	#return p
	
#n,m = input().strip().split(' ')#n is no. of people
#n,m = [int(n), int(m)]# m is no. of topics
#topchart=[]#chart of topics who knows who don't
#for i in range(n):
	#temp = list(input().strip())
	#topchart.append(temp)
#teamchart={}# this is awesome! team as key and their correspoing no. of topics as values
#for i in range(n):# i is each person
	#for j in range(i+1,n):# j's are other persons who can team-up with i
		#temp=topchart[i]# to hold the team topic chart of i with j
		#print(topchart[i])
		#for index,k in enumerate(topchart[j]):
			#if k == '1' and temp[index]!='1':
				#temp.pop(index)
				#temp.insert(index, '1')
		##for loop ke bahar aane par i has got his team topic chart, i.e. temp.
		#print(temp,'\n')
		#max=onesearch(temp)
		#teamchart[(i,j)]=max# storing the info of team (i,j) and their total no. of topics
##print(teamchart)
#max_topics, max_teams=0,0
#for i in teamchart:
	#if max_topics< teamchart[i]:
		#max_topics = teamchart[i]
		#max_teams+=1
#print(max_topics)
#print(max_teams)
