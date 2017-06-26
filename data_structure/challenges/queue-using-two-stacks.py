class stack(object):
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.insert(0, element)

    def pop(self):
        return self.array.pop(0)

    def isEmpty(self):
        return False if self.array else True

    def peek(self):
        return self.array[0]

def flip(oldestOnTop, newestOnTop):
    while not newestOnTop.isEmpty():
        oldestOnTop.push(newestOnTop.pop())

oldestOnTop = stack()
newestOnTop = stack()

q = int(input().strip())
for _ in range(q):
    inp = input().strip().split(' ')
    if inp[0] == '1':
        newestOnTop.push(inp[1])
    elif inp[0] == '2':
        if oldestOnTop.isEmpty():
            flip(oldestOnTop, newestOnTop)
        oldestOnTop.pop()
    else:
        if oldestOnTop.isEmpty():
            flip(oldestOnTop, newestOnTop)
        print(oldestOnTop.peek())
