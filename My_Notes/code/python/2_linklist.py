class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def find_by_value(self, value):
        p = self.head
        while p and p.data != value:
            p = p.next
        return p

    def find_by_index(self, index):
        p = self.head
        position = 0
        while p and position != index:
            p = p.next
            position += 1
        return p

    def insert_to_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
