    #https://www.hackerrank.com/challenges/countingsort3
    n = int(input())
    a = []
    for i in range(n):
        j = int(input().strip().split(' ')[0])
        a.append(j)
    ans = []
    for i in range(100):
        ans.append(sum([j <= i for j in a]))

    print(" ".join(map(str, ans)))
