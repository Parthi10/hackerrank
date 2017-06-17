import time
t = int(input())
def listS1(s1,s2,a,b,l1,l2):
    try:
        print("got",a,b)
        if (s1[a+1]) < (s2[b+1]):
            return True
        elif (s1[a+1]) > (s2[b+1]):
            return False
        else:#both equal yet again ,,time for recursion!!
            if a+2<l1 and b+2<l2:
                return listS1(s1,s2,a+1,b+1,l1,l2)
            elif a+2 == l1 and b+2 < l2: #a is pointing to last index of s1
                return listS1(s1,s2,a,b+1,l1,l2)
            elif b+2 == l2 and a+2 < l1:
                return listS1(s1,s2,a+1,b,l1,l2)
            else:#both are at the end
                return True #choose any list doesn't matter
    except Exception as e:
        print(e)
        time.sleep(10)

final_ans = []
for i in range(t):
    s1 = input().strip()
    s2 = input().strip()
    l1 = len(s1)
    l2 = len(s2)
    length = l1 +l2
    x,a,b = [0]*3
    ans = ""
    while x < length:
        if a < l1 and b < l2:
            if (s1[a]) < (s2[b]):
                ans+= s1[a]
                a += 1
            elif (s1[a]) > (s2[b]):
                ans += s2[b]
                b += 1
            else: #both equal check which side to move
                if a+1 < l1 and b+1 < l2:
                    if listS1(s1,s2,a,b,l1,l2):
                        ans += s1[a]
                        a += 1
                    else:
                        ans+= s2[b]
                        b += 1
                else:#ANY ONE OF a n b at last index, both last char same
                    if a+1<l1 and b+1 > l2:#b at last
                        ans+=s1[a]#why that?? irrespective of next elem of s1 it will work
                        a+=1
                    else:#a at last
                        ans+=s2[b]
                        b+=1
            x+=1
        elif a<l1 and b+1>l2:
            #s2 is exhausted
            ans += s1[a:]
            break
        elif b<l2 and a+1>l1:
            #s1 is exhausted
            ans += s2[b:]
            break
    final_ans.append(ans)

print("\n".join(final_ans))
