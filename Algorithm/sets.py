(input())
m=set(int(x) for x in input().strip().split(' '))
(input())
n=set(int(x) for x in input().strip().split(' '))
#p=n.symmetric_difference(m)

r=(m|n)-(m&n)
print(sorted(r))
print(sorted(p-q))

