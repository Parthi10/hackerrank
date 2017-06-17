import sys
sys.setrecursionlimit(15000)

class Node(object):
    def __init__(self, left_node=None, right_node=None, data=None):
        self.left = left_node
        self.right = right_node
        self.data = data


n = int(input().strip())

nodes = [Node(data=i) for i in range(1, n+1)]

for i in range(n):
    a, b = map(int, input().strip().split(' '))
    if a != -1:
        nodes[i].left = nodes[a-1]
    if b != -1:
        nodes[i].right = nodes[b-1]



def swapTheChildren(node):
    node.left, node.right = node.right, node.left

def printInorderTraversal(root):
    if root:
        printInorderTraversal(root.left)
        print(root.data, end=" ")
        printInorderTraversal(root.right)

def swapping(root, k, depth_of_root=1):
    if root:
        if depth_of_root % k == 0:
            swapTheChildren(root)
        depth_of_root += 1
        swapping(root.left, k, depth_of_root=depth_of_root)
        swapping(root.right, k, depth_of_root=depth_of_root)


t = int(input().strip())
for _ in range(t):
    k = int(input().strip())
    swapping(nodes[0], k)
    printInorderTraversal(nodes[0])
    print()
