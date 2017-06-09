class stack(object):
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.insert(0, element)

    def pop(self):
        self.array.pop(0)

    def isEmpty(self):
        return bool(len(self.array))

    def top(self):
        return self.array[0]

        
