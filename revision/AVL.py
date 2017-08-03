class Node(object):
    def __init__(self, data=None, height=None):
        self.data = data
        self.height = height
        self.left = None
        self.right = None

class AVL(object):
    def __init__(self):
        self.root = None

    def leftRotate(self, root):
        temp = root.right
        temp.left = root
        root.right = temp.left
        self.setHeight(root)
        self.setHeight(temp)
        return temp

    def rightRotate(self, root):
        temp = root.left
        temp.right = root
        root.left = temp.right
        self.setHeight(temp)
        self.setHeight(root)
        return temp

    def getHeight(self, root):
        return root.height if root else -1

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def setHeight(self, root):
        root.height = 1 + max(self.getHeight(root.left),
                                    self.getHeight(root.right))

    def insert(self, data, root=self.root):
        if root=None:
            return Node(data=data, height=0)
        elif data > root.data:
            root.left = self.insert(data, root.left)
        else:
            root.right = self.insert(data, root.right)

        balance = self.getBalance(root)
        if balance > 1:
            if self.getBalance(root.left) < 0:#LR
                root.left = self.leftRotate(root.left)
            root = self.rightRotate(root)

        elif balance < -1:
            if self.getBalance(root.right) > 0:#RL
                root.right = self.rightRotate(root.right)
            root = self.leftRotate(root)
        else:
            self.setHeight(root)
        return root
