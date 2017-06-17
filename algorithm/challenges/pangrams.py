string=str(input().strip())
alphabet=[0]*26#to check each alphabet
count=0
for i in string:
    if(i!=' '):#ascii of space is 35 so ignore it
        y=ord(i)# ascii value of i
        if(y>=97):#lower case
            alphabet[y-97]=1# ascii of lower case starts from 97
        elif(y<=90):#upper case
            alphabet[y-65]=1#ascii of upper case starts from 65
for i in alphabet:
    if(i==1):
        count+=1
if(count==26):# means all alphabets are present
    print('pangram')
else:
    print('not pangram')
