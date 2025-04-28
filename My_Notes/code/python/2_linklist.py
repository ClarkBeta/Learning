class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def find_by_value(self, value: int):
        p = self.head
        while p and p.data != value:
            p = p.next
        return p

    def find_by_index(self, index: int):
        p = self.head
        position = 0
        while p and position != index:
            p = p.next
            position += 1
        return p

    def insert_before(self, index: int, node: Node, value: int):
        if self.find_by_index(index) == self.head:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(value)
            new_node.next = node.next
