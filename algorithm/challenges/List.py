#https://www.hackerrank.com/challenges/python-lists
#getattr(Object, Function)(Vars)
L=[]
t= int(input())
for i in range(t):
    arg=input().strip().split(' ')
    if(arg[0]=='print'):
       print(L)
    elif(len(arg)==2):
        getattr(L, arg[0])(int(arg[1]))
    elif(len(arg)==3):
        getattr(L,arg[0])(int(arg[1]),int(arg[2]))
    else:
        getattr(L,arg[0])()
