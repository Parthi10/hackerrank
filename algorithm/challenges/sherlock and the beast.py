t = int(input().strip())
ansList=[0]*t
for a0 in range(t):
    n = int(input().strip())
    if(n%3==0 and n%5!=0):
        ansList[a0]='5'*n
    elif(n%3!=0 and n%5==0):
        ansList[a0]='3'*n
    elif(n%3==0 and n%5==0):
        ansList[a0]='5'*(n//3)+'3'*(n//5)        
    else:
        i3=n//3
        if(i3==0):
            ansList[a0]=-1
        else:            
            for i in range(i3,0,-1):
                if((n-i*3)%5==0):
                    ansList[a0]='5'*(i*3)+'3'*(n-i*3)
                    break
                else:
                    ansList[a0]=-1
        
for i in ansList:
    print(i)
'''try this:
t=int(input())
for i in range(t):
    y=int(input())
    z=y
    while(z%3!=0):
        z-=5
    if(z<0):
        print('-1')
    else:
        print('5'*z+(y-z)*'3')

'''
