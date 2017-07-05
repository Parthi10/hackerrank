def play(n):
    moves = 0
    while n != 1:
        if n & (n-1) == 0:#n is of the form 2**x
            n >>= 1# reduce it to half
        else:
            n -= 1 << (n.bit_length() - 1)
        moves += 1
    if moves%2==0:
        print('Richard')
    else:
        print('Louise')

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    play(n)
