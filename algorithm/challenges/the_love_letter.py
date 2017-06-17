#task is make palindromes of given string input
#https://www.hackerrank.com/challenges/the-love-letter-mystery
#print minimum no. of steps required to do so
t=int(input())
ans=[]
for i in range(t):
    s=[ord(a) for a in input().strip()]#store ascii values
    n=len(s)
    count=0
    print(s,n)
    if(n%2==0): #even
        for i in range(0,n//2):
            count+=abs(s[i]-s[(n-1)-i])#store the difference which is equal to no. of steps
            print('even', count)
    else:#odd
        for i in range(0,(n-1)//2):
            count+=abs(s[i]-s[(n-1)-i])#same as above
            print('odd', count)
    ans.append(count)       
for i in ans:
    print(i)
