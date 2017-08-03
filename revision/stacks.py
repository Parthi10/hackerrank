class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.insert(0, data)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]
