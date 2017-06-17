import time
final_ans = []
t = int(input())
for i in range(t):
    s1 = input().strip()
    s2 = input().strip()
    l1 = len(s1)
    l2 = len(s2)
    length = l1 +l2
    a,b=0,0
    ans = ""
    while a < l1 and b<l2:
        if s1[a:] + "z" <= s2[b:] +"z":
            ans+=s1[a]
            a+=1
        else:
            ans+=s2[b]
            b+=1

    ans+= s1[a:]+s2[b:]
    final_ans.append(ans)

print("\n".join(final_ans))
