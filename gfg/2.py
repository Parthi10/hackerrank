#http://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
t = int(input().strip())
for _ in range(t):
    n, s = map(int, input().strip().split())
    arr = [int(x) for x in input().strip().split(' ')]
    m = min(arr)
    array = [x for x in arr if (x+m) <s]
    array.sort()
    ans = 0
    n = len(array)
    for i in range(n-2):
        j = i+1
        k = n-1
        while(j<k):
            if array[i] + array[j] + array[k]>=s:
                k-=1
            else:
                ans+=(k-j)
                j+=1
    print(ans)
