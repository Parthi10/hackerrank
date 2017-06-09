s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

appleCount, orangeCount = 0,0
for i in apple:
    if i > 0:
        if a+i >= s and a+i <= t:
            appleCount += 1
for i in orange:
    if i < 0:
        if b+i >= s and b+i <= t:
            orangeCount += 1

print(appleCount)
print(orangeCount)
