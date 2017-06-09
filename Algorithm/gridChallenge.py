#https://www.hackerrank.com/challenges/grid-challenge
t=int(input().strip())
ans=[0]*t
for i in range(t):
    n=int(input().strip())
    mainList=[]
    for z in range(n):
        l=list(input().strip()) #analyse closely, its awesome
        mainList.append(sorted(l))#sorted lexicographically
#done with input
    for x in range(n):
        l=[]
        for y in range(n):
            l.append(mainList[y][x])# make a sublist of columns 
        if(l==sorted(l)):#condition of question
            ans[i]='YES'
        else:
            ans[i]='NO'
            break
for i in ans:    
    print(i)            
            
