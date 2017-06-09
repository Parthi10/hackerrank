a=[]
t = int(input().strip())
for a0 in range(t):
    n = input()
    count = 0
    for i in n:
        # if(int(i)!=0):
        #     print(i)
        if(int(i)!=0 and int(n)%int(i)==0 ):
            count=count+1
    a.append(count)
for i in a:
    print(i)
