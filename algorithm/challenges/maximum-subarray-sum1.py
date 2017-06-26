def modified_kadanes(a, n, m):

    modulo_prefix_array = [a[0]]
    for i in range(1, n):
        modulo_prefix_array += [(a[i] % m + modulo_prefix_array[i-1]) % m]

    # print(modulo_prefix_array)
    ans = 0
    for i in range(n):
        for j in range(i-1,-1, -1):
            ans = max(ans, (modulo_prefix_array[i]-modulo_prefix_array[j] +m )%m)
        ans = max(ans, modulo_prefix_array[i])
    return ans

q = int(input().strip())
for _ in range(q):
    n, m = map(int, input().strip().split(' '))
    a = [int(x) for x in input().strip().split(' ')]
    print(modified_kadanes(a, n, m))
