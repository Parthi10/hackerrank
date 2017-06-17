class stack(object):
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.insert(0, element)

    def pop(self):
        self.array.pop(0)

    def top(self):
        if self.array != []:
            return self.array[0]
        return 0 #x>0

s = stack()

n = int(input().strip())

for _ in range(n):
    inp = list(map(int, input().strip().split(' ')))
    if inp[0] == 1:
        s.push(max(inp[1], s.top())) #we gotta return the max value in the stack only. not what's on top, the ques doesn't ask that. :P or else maintain another max stack
    elif inp[0] == 2:
        s.pop()
    else:
        print(s.top())
