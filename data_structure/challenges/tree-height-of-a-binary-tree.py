class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    if root.left and root.right:
        return 1 + max(height(root.left), height(root.right))
    elif root.left:
        return 1
    elif root.right:
        return 1
    else:
        return 0

tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)

print(height(tree.root))

'''
#alternate solution

def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1

def getTreeHeight(node):
    return  1 + max(getTreeHeight(node.left), getTreeHeight(node.right)) if node else -1

'''
