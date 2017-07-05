l = [1,2,3,4]

def printCombo(l):
    for j in range(1, len(l)+1):
        for i in range(len(l)-1):
            l[i],l[i+1]=l[i+1],l[i]
            print(l)

for i in range(len(l)):
    printCombo(l[i:])
