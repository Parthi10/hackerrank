class Node(object):

    def __init__(self, data=None, height=None):
        self.data = data
        self.height = height
        self.leftChild = None
        self.rightChild = None

class Tree(object):

    def __init__(self):
        pass

    def rightRotate(self, root):
        LNode = root.leftChild
        root.leftChild = LNode.rightChild
        LNode.rightChild = root
        root.height = self.setHeight(root)
        LNode.height = self.setHeight(LNode)
        return LNode

    def leftRotate(self, root):
        RNode = root.rightChild
        root.rightChild = RNode.leftChild
        RNode.leftChild = root
        root.height = self.setHeight(root)
        RNode.height = self.setHeight(RNode)
        return RNode

    def setHeight(self, root):
        return 1 + max(self.height(root.leftChild), self.height(root.rightChild))

    def height(self, root):
        return root.height if root else -1

    def balance(self, root):
        return self.height(root.leftChild) - self.height(root.rightChild)

    def insert(self, data, root):
        if root == None:
            return Node(data=data, height=0)
        elif data >= root.data:
            root.rightChild = self.insert(data, root.rightChild)
        else:
            root.leftChild = self.insert(data, root.leftChild)

        BF = self.balance(root)

        if BF > 1: #L-L OR L-R
            if balance(root.leftChild) < 0:
                root.leftChild = leftRotate(root.leftChild)
            root = self.rightRotate(root)

        elif BF < -1:#R-R OR R-L
            if balance(root.rightChild) > 0:
                root.leftChild = self.rightRotate(root.rightChild)
            root = self.leftRotate(root)
        else:
            root.height = self.setHeight(root)

        return root


Tree = Tree()
r1 = Tree.insert(3, root=None)
r2 = Tree.insert(2, root=r1)
r3 = Tree.insert(4, root=r2)
root = Tree.insert(5, root=r3)
print(root.data)
print(root.leftChild.data, root.rightChild.data)
print(root.rightChild.rightChild.data)
root = Tree.insert(6, root=root)
print()
print(root.data)
print(root.leftChild.data, root.rightChild.data)
print(root.rightChild.leftChild.data, root.rightChild.rightChild.data)

print()
print(root.height)
print(root.leftChild.height, root.rightChild.height)
print(root.rightChild.leftChild.height, root.rightChild.rightChild.height)
