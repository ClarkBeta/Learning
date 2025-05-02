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

    def insert_before(self, index: int, value: int):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            position = 0
            while current and position < index - 1:
                current = current.next
                position += 1
            if not current:
                raise IndexError("Index out of range")
            new_node.next = current.next
            current.next = new_node

    def delete_by_index(self, index: int):
        if not self.head:
            raise IndexError("Index out of range (empty list)")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            position = 0
            while current and position < index - 1:
                current = current.next
                position += 1
            if not current or not current.next:
                raise IndexError("Index out of range")
            current.next = current.next.next

    def delete_by_value(self, value: int):
        if not self.head or not value:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        pre = self.head
        node = self.head.next
        not_found = False
        while node.data != value:
            if node.next:
                not_found = True
                break
            else:
                pre = node
                node = node.next
        if not not_found:
            pre.next = node.next

    def print_all(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        print(f"{current.data}", end="")
        current = current.next
        while current:
            print(f"->{current.data}", end="")
            current = current.next
        print()


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_before(0, 1)  # 链表: 1
    llist.insert_before(0, 2)  # 链表: 2->1
    llist.insert_before(1, 3)  # 链表: 2->3->1
    llist.insert_before(3, 4)  # 链表: 2->3->1->4
    llist.delete_by_index(0)  # 删除 2，链表变为 3->1->4
    llist.delete_by_value(3)
    llist.print_all()  # 输出: 3->1->4
