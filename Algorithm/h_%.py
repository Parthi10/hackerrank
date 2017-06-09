'''Input Format

The first line contains the integer NN, the number of students.
The next NN lines contains the name and marks obtained by that
student separated by a space. The final line contains the name of
a particular student previously listed.

Output Format

Print one line: The average of the marks obtained by the particular
student correct to 2 decimal places.'''
n=int(input())
dict={}
numList=[]
nameList=[]
for i in range(0,n):
    name,a,b,c=input().split()
    name=str(name)
    a=float(a)
    b=float(b)
    c=float(c)
    numList.append((a+b+c)/3)
    nameList.append(name)
for i in range(0,n):
    dict[nameList[i]] = numList[i]
new=str(input())
if(new in dict):
    print("%.2f" %dict[new])

    
