from collections import defaultdict

n, m = map(int, input().strip().split(' '))
mat = [[x for x in input().strip().split(' ')] for y in range(n)]

def get_the_digits(x1, y1, x2, y2):
    digits = []
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            digits.append(mat[x][y])
    return digits

def check_palindrome(digits):
    digit_count = defaultdict(int)
    for digit in digits:
        digit_count[digit] += 1
    odd_count = 0
    for digit in digit_count:
        if digit_count[digit] & 1: #digit_count[digit] is odd
            odd_count += 1
    if odd_count <= 1:
        return True
    else:
        return False
ans_max = 0

for x2 in range(n-1, -1, -1):
    for y2 in range(m-1, -1, -1):
        print(x2, y2)
        digits = get_the_digits(0,0,x2, y2)
        if check_palindrome(digits):
            l = len(digits)
            if ans_max < l:
                ans_max = l
                cordi = [0,0, x2, y2]
print(ans_max)
print(" ".join(map(str, cordi)))
