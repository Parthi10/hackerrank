from itertools import combinations_with_replacement
n,m = map(int, input().strip().split(' '))
coin_list = [int(x) for x in input().strip().split(' ')]
import time
t = time.time()
chache = []

def main(coin_list,n):
    chache.append([coin_list,n])
    print("got a list", coin_list,n)
    L = len(coin_list)
    count = 0
    if L==0:
        return 0
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n > 0:
        # if time.time()-t>10:
        #     print("time UP")
        #     return None
        if [coin_list, n - coin_list[-1]] not in chache:
            count += main(coin_list, n - coin_list[-1])
        if [coin_list[:L-1], n] not in chache:
            count += main(coin_list[:L-1], n) #solution after n is subtracted by last coin+#solution without last coin
    return count
print(main(coin_list,n))
