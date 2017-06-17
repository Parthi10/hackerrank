from itertools import combinations as combo
t = int(input().strip())

for _ in range(t):
    string = input().strip()
    k = int(input().strip())
    substrings = ([string[i:j] for i,j in combo(range(len(string)+1),2)])
    ans = "".join(substrings)
    print(ans[k-1])
