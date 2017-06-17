class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node #another Node instance

class LinkedList(object):

    def __init__(self, first_node):
        self.root_node = first_node
        self.tail_node = first_node #
        self.size =  1

    def prepend_node(self, node_to_be_prepended):
        root_node = self.root_node
        node_to_be_prepended.next_node = root_node
        self.root_node = node_to_be_prepended
        self.size += 1

    def append_node(self, node_to_be_appended):
        tail_node = self.tail_node
        tail_node.next_node = node_to_be_appended
        self.tail_node = node_to_be_appended
        self.size += 1

    def remove_node(self, data):
        this_node = self.root_node
        previous_node = None
        while this_node: #will become false at tail_node
            if data == this_node.data:
                if previous_node:
                    previous_node.next_node = this_node.next_node
                else: #this_node is root_node
                    self.root_node = this_node.next_node
                self.size -= 1
                return True
            else:
                previous_node = this_node
                this_node = this_node.next_node
        return False

    def find_node(self, data):
        this_node = self.root_node
        previous_node = None
        while this_node:
            if this_node.data == data:
                return this_node
            else:
                previous_node = this_node
                this_node = this_node.next_node
        return None
