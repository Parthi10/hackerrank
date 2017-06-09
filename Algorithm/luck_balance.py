n, k = input().strip().split(' ')
n, k = int(n), int(k)

imp_contests = 0
imp = []
nimp = []
for i in range(n):
    l, t = input().strip().split(' ')
    l, t = int(l), int(t)
    if t == 1:
        imp.append([l,t])
    else:
        nimp.append([l,t])
imp.sort()
ans = 0
ans_subtract = 0

for i in range(len(imp)-k):
    ans_subtract += imp[i][0]
    del imp[i]
for i in range(len(imp)):                                                
    ans += imp[i][0]
for i in range(len(nimp)):
    ans += nimp[i][0]
print(ans-ans_subtract)
