class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def appendNode(self, new_node):
        node = self.head

        if not node:
            self.head = new_node
            return

        while node:
            prevNode = node
            node = node.next

        prevNode.next = new_node

    def findNode(self, node):
        temp_node = self.head
        while temp_node:
            if temp_node == node:
                return True
            temp_node = temp_node.next
        return False

    def prependNode(self, node):
        if self.head:
            node.next = self.head
        self.head = node

    def insertNode(self, data):
        new_node = Node(data)
        node = self.head
        if not node:
            self.head = new_node
            return

        if node.data > data:
            self.head = new_node
            new_node.next = node
            return

        while node and node.data < data:
            previous_node = node
            node = node.next

        previous_node.next = new_node
        new_node.next = node

    def deleteNode(self, node):#given the node in LL
        temp_node = self.head
        if temp_node==node:
            self.head = self.head.next
            return

        while temp_node:
            if temp_node == node:
                previous_node.next = temp_node.next
                break
            previous_node = temp_node
            temp_node = temp_node.next
