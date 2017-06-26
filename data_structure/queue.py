class Queque(object):

    def __init__(self):
        self.queque = []

    def inQueque(self, element):
        self.queque.insert(0, element)

    def deQueue(self):
        return self.queque.pop()

    def isEmpty(self):
        return bool(len(self.queque))

    def peek(self):
        return self.queque[-1]
