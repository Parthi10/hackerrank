"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
class Queue(object):
    def __init__(self):
        self.queque = []
    def put(self, some_shit):
        self.queque.append(some_shit)
    def get(self):
        return self.queque.pop(0)
    def empty(self):
        return bool(self.queque == [])


def levelOrder(root, virgin=True):
    q = Queue()
    if virgin:
        q.put(root)
    while not q.empty():
        node = q.get()
        print node.data
        q.put(node.left)
        q.put(node.right)
        levelOrder(node, virgin=False)
