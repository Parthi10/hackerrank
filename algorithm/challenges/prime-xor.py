q = int(input().strip())
primes = defaultdict(lambda:None)

for _ in range(q):
    n = int(input().strip())
    num = map(int, input().strip().split(' '))
    
