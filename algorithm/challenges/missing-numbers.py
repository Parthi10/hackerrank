from collections import defaultdict

n = int(input().strip())
n_dict = defaultdict(int)
for x in input().strip().split(' '):
    n_dict[x] += 1


m = int(input().strip())
m_dict = defaultdict(int)
for x in input().strip().split(' '):
    m_dict[x] += 1

missing_numbers = defaultdict(int)
for i in m_dict:
    diff = m_dict[i] - n_dict[i]
    if diff:
        missing_numbers[i] =  diff

for i in sorted(missing_numbers):
    print(i, end=" ")
