from collections import defaultdict

f_values = defaultdict(lambda:None)
f_values[0] = f_values[1] = 1
def get_f_value(i):
    if not f_values[i]:
        f_values[i] = get_f_value(i-1) + get_f_value(i-2)
    return f_values[i]

graph = defaultdict(list)
value_map = defaultdict(int)

n = int(input().strip())
for _ in range(n):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

c = map(int, input().strip().split())
for i, value in enumerate(c)
    value_map[i+1] = value
