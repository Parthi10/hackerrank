s = list(input().strip())
def reduce(s):
    x = 0
    while x<len(s):
        try:
            if s[x] == s[x+1]:
                s.pop(x)
                s.pop(x)
                reduce(s)
        except:
            break
        x += 1
reduce(s)

if s!=[]:
    for i in s:
        print(i,end="")
else:
    print('Empty String')
