n = int(input())
day = 1
ads = 5
likes = 0
while day <= n:
    likes += (ads // 2)
    ads = (ads//2) *3
    # print(likes, day)
    day += 1

print(likes)
