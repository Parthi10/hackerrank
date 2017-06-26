n, k = map(int, input().strip().split(' '))
impContests = []
luck_balance=0
for i in range(n):
    inp = input().strip().split(' ')
    luck = int(inp[0])
    imp = int(inp[1])
    luck_balance += luck
    if imp:
        impContests.append(luck)
impContests.sort()

m = len(impContests)
for i in range(m-k):
    luck_balance -= impContests[i]

print(luck_balance)
