import operator from itemgetter
t=int(input())
ladList=[]
SnakeList=[]
def shortestmove(ladList, SnakeList):
	ladList=sorted(ladList)
	SnakeList=sorted(SnakeList)
	step=0
	
	
	
	
	
	
	
for i in range(t):
    L=int(input())
    for i in range(L):
        a=[int(temp) for temp in input().strip().split(" ")]
        ladList.append(a)
    S=int(input())
    for i in range(S):
        a=[int(temp) for temp in input().strip().split(" ")]
        SnakeList.append(a)
	shortestmove(ladList, SnakeList)


